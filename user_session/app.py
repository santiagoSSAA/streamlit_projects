import streamlit as st
from services.user_service import UserService
from streamlit_cookies_manager import EncryptedCookieManager
from dotenv import load_dotenv
import os
from views import home_view, login_view, signup_view, logged_in_view

# Load environment variables from .env file
load_dotenv()

# Retrieve cookie settings from environment variables
cookie_prefix = os.getenv("COOKIE_PREFIX")
cookie_password = os.getenv("COOKIE_PASSWORD")

# Initialize cookies manager
cookies = EncryptedCookieManager(
    prefix=cookie_prefix,  # Prefix for cookie names
    password=cookie_password  # Use a secure password
)

if not cookies.ready():
    st.stop()

def initialize_session():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = cookies.get("logged_in", "False") == "True"
        st.session_state.username = cookies.get("username", "")

def handle_logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    cookies["logged_in"] = "False"
    cookies["username"] = ""
    cookies.save()
    st.rerun()

def main():
    initialize_session()

    # Set the title of the landing page
    st.title("Welcome to My Streamlit App")

    # Create users table
    UserService.create_users_table()

    if st.session_state.logged_in:
        logged_in_view.display(st.session_state.username, handle_logout)
    else:
        # User registration and login
        menu = ["Home", "Login", "SignUp"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Home":
            home_view.display()
        elif choice == "Login":
            login_view.display(UserService, cookies)
        elif choice == "SignUp":
            signup_view.display(UserService)

if __name__ == "__main__":
    main()
