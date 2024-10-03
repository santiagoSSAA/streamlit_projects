import streamlit as st
import openai
from fpdf import FPDF
import re
from datetime import datetime
import unidecode
from st_paywall import add_auth

add_auth(required=True)

# Load API key from secrets.toml
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Validate user input


def validate_input(user_text):
    if len(user_text) > 500:
        st.warning("Text cannot exceed 500 characters.")
        return False
    if not re.match("^[A-Za-z0-9,.?!' ]+$", user_text):
        st.warning("Text contains invalid characters.")
        return False
    return True

# Clean input text by removing special characters and accents


def clean_text(text):
    return unidecode.unidecode(text)

# Generate detailed action plan using OpenAI


def generate_detailed_plan(prompt, days, time_format):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Create a detailed action plan for {prompt}, structured in {days} {time_format}. "
                           "The format should be:\n\n"
                           f"""[Day/week/month Number (depending on your logic)]. [Short, descriptive title of the Day/week/month's goal]

- Tasks
    - [Clear, detailed description of task #1]
    - [Clear, detailed description of task #2]
    - ...

- Estimated duration: [Duration]
- Objective: [Clear description of the selected time period objective]

(Make this individually by Day/week/month (depends of your logic) until cover the whole available time.)

.\n.\n.\n"""
                           "Follow a professional and motivating writing standard. Write your answer strictly in english. Avoid non 'latin1' characters for your writing."
            }
        ]
    )
    return response.choices[0].message.content

# Create a PDF with the detailed plan


def create_pdf(plan, user_name, plan_type, days, time_format):
    pdf = FPDF()
    pdf.add_page()

    # Headers for the document
    headers = ["Action Plan", "Generated for", "Duration", "Date"]
    unit_time_text = {
        "Days": "Days",
        "Weeks": "Weeks",
        "Months": "Months"
    }[time_format]

    # Document header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, f"{headers[0]}: {plan_type}", ln=True, align='C')
    pdf.cell(200, 10, f"{headers[1]}: {user_name}", ln=True, align='C')
    pdf.cell(
        200, 10, f"{headers[2]}: {days} {unit_time_text}", ln=True, align='C')
    pdf.cell(
        200, 10, f"{headers[3]}: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align='C')

    pdf.ln(10)  # Blank line

    # Plan content
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, plan)

    return pdf


# User interface
st.title("AI Action Plan Generator")
st.markdown("""
    Enter a description of your idea or goal, select the type of plan and available time, 
    and we'll help you generate a detailed action plan with time estimates.
""")

# Additional fields for customization
user_name = st.text_input("Your name:")
plan_type = st.selectbox("Select the type of plan:", [
                         "Entrepreneurship", "Personal Goal"])
user_text = st.text_area("Describe your idea or goal:")

# Time selection limited to 1-10 for days, weeks, or months
time_range = st.selectbox("Select the time unit:", ["Days", "Weeks", "Months"])
time_plan = st.number_input("How many?", min_value=1, max_value=10, value=1)

# Validate input and generate the plan
if st.button("Generate PDF"):
    if user_text and user_name:
        cleaned_text = clean_text(user_text)  # Clean the input text
        if validate_input(cleaned_text):
            # Generate detailed plan
            detailed_plan = generate_detailed_plan(
                cleaned_text, time_plan, time_range.lower())

            if detailed_plan:
                # Create customized PDF
                pdf = create_pdf(detailed_plan, user_name,
                                 plan_type, time_plan, time_range)
                pdf_output = f"action_plan_{user_name}.pdf"
                pdf.output(pdf_output)

                # Download the PDF
                with open(pdf_output, "rb") as f:
                    st.download_button(
                        "Download Action Plan", f, file_name=pdf_output, mime="application/pdf")
            else:
                st.warning("Failed to generate the plan due to an error.")
        else:
            st.warning("Please fill in all fields.")

# Session request limit to avoid abuse
if 'requests' not in st.session_state:
    st.session_state['requests'] = 0

if st.session_state['requests'] > 10:
    st.error(
        "You have reached the request limit for this session. Please try again later.")
else:
    st.session_state['requests'] += 1
