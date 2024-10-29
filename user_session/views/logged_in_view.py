import streamlit as st

def display(username, handle_logout):
    st.subheader(f"Welcome {username}!")
    st.write("You are logged in.")
    if st.button("Logout"):
        handle_logout() 