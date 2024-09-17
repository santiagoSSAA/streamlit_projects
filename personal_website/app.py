"""This module contains a streamlit personal website"""

from threading import local
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# For more emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="My website", page_icon="🥳", layout="wide")

# --- LOAD ASSESSTS ---
LOTTIE_CODING = "https://lottie.host/bd2bd652-c5ae-4aa0-b48d-e94f2287f83c/WtydDibywx.json"
IMG_BUGDET_BIGDATA = Image.open("images/budget_bigdata.jpeg")
IMG_STOCK_AI = Image.open("images/stock_ai.jpeg")


def load_lottieurl(url):
    """Function for getting url lottie file animation from a API request"""
    request = requests.get(url, timeout=15)
    if request.status_code != 200:
        return None
    return request.json()

# Use local CSS


def local_css(file_name):
    """Function to load local css style for submit form"""
    with open(file_name, encoding="utf-8") as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# --- HEADER SECTION ---


with st.container():
    st.subheader("Hi, I am Santiago! 🧑‍💻")
    st.title("A Data Engineer from Colombia!")
    st.write(
        "I am passionate about finding new creative ways to use Data and Software, more than just a company scope."
    )
    st.write("[Learn More >](https://github.com/santiagoSSAA)")

# --- WHAT I DO ---

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(
            """
            - **Design and Develop Data Architectures:** Create scalable data architectures and manage data pipelines to handle large datasets efficiently.
            - **Manage ETL Processes:** Develop and optimize ETL (Extract, Transform, Load) processes to ensure data accuracy and efficiency.
            - **Integrate Data Sources:** Work with various data sources to create seamless integrations and ensure data consistency.
            - **Backend Development:** Enjoy working on backend systems, designing architectures that complement the data pipelines and structures.
            - **Experiment with Data and Software:** I love discovering fun and quirky ways to leverage data and software, always looking for innovative approaches without losing sight of the core focus: creating efficient and scalable data solutions.
            
            If this sound interesing, consider check my LinkedIn to get in touch!.
            
            [Linkedin >](https://www.linkedin.com/in/santiagossaa/)
            """
        )
    with right_column:
        st_lottie(LOTTIE_CODING, height=500, key="coding")

# --- PROJECTS ---
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(IMG_BUGDET_BIGDATA)
    with text_column:
        st.subheader(
            "Budget-Friendly Big Data Analysis: Python & Google Colab On an Everyday Laptop")
        st.write(
            """
            On this article, I explain how to make an ETL for manage big amounts of data from a simple budget laptop!.
            """
        )
        st.markdown(
            "[Read Article...](https://azumo.com/insights/budget-friendly-big-data-analysis-python-google-colab-on-everyday-laptop)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(IMG_STOCK_AI)
    with text_column:
        st.subheader(
            "Web application for predicting Stock Prices: Python, Flask & TensorFlow | Part 1")
        st.write(
            """
            On this article, I give an initial approach to an exciting AI project for predicting stocks market using AI!.
            """
        )
        st.markdown(
            "[Read Article...](https://azumo.com/insights/web-application-for-predicting-stock-prices-python-flask-tensorflow)")

# --- CONTACT ---

# Documentation: https://formsubmit.co/ ¡¡¡CHANGE EMAIL ADDRESS!!!
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    CONTACT_FORM = """
    <form action="https://formsubmit.co/santiago.sanchez.ssaa@gmail.com" method="POST">
        <input type="hidden" name"_captcha" value"false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(CONTACT_FORM, unsafe_allow_html=True)
    with right_column:
        st.empty()
