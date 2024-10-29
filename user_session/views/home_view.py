import streamlit as st

def display():
    # Inject custom CSS
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 3em;
            color: #4CAF50;
            text-align: center;
            margin-top: 20px;
        }
        .subheader {
            font-size: 1.5em;
            color: #555;
            text-align: center;
            margin-bottom: 30px;
        }
        .features, .benefits, .cta, .contact {
            margin: 20px 0;
            padding: 10px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .cta-button {
            display: block;
            width: 200px;
            margin: 20px auto;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            text-align: center;
            border-radius: 5px;
            text-decoration: none;
        }
        .cta-button:hover {
            background-color: #45a049;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    st.markdown('<div class="main-title">Welcome to AI SaaS</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Revolutionizing Your Business with AI</div>', unsafe_allow_html=True)

    # Hero section
    st.image("https://via.placeholder.com/800x300", caption="AI SaaS - Transforming the Future", use_column_width=True, output_format="auto")

    # Key features
    st.markdown('<div class="features">', unsafe_allow_html=True)
    st.markdown("## Key Features")
    st.markdown("""
    - **Automated Insights**: Leverage AI to gain insights from your data effortlessly.
    - **Scalable Solutions**: Our platform grows with your business needs.
    - **User-Friendly Interface**: Designed for ease of use, no technical expertise required.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Benefits
    st.markdown('<div class="benefits">', unsafe_allow_html=True)
    st.markdown("## Benefits")
    st.markdown("""
    - **Increase Efficiency**: Automate routine tasks and focus on strategic initiatives.
    - **Cost-Effective**: Reduce operational costs with AI-driven solutions.
    - **Data-Driven Decisions**: Make informed decisions with real-time analytics.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Call to action
    st.markdown('<div class="cta">', unsafe_allow_html=True)
    st.markdown("## Get Started Today!")
    st.write("Sign up now to start your free trial and see the difference AI can make.")
    if st.button("Sign Up Now"):
        st.experimental_rerun()  # Redirect to sign-up page or functionality
    st.markdown('</div>', unsafe_allow_html=True)

    # Contact information
    st.markdown('<div class="contact">', unsafe_allow_html=True)
    st.markdown("## Contact Us")
    st.write("For more information, contact us at [info@aisaas.com](mailto:info@aisaas.com).")
    st.markdown('</div>', unsafe_allow_html=True)