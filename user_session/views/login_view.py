import streamlit as st

def display(UserService, cookies):
    st.subheader("Login Section")

    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if UserService.verify_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            cookies["logged_in"] = "True"
            cookies["username"] = username
            cookies.save()
            st.success(f"Welcome {username}!")
            st.rerun()
        else:
            st.error("Invalid username or password") 