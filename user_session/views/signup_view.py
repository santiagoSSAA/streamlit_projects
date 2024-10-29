import streamlit as st

def display(UserService):
    st.subheader("Create New Account")

    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')

    if st.button("SignUp"):
        if UserService.add_user(new_user, new_password):
            st.success("You have successfully created an account")
            st.info("Go to Login Menu to login")
        else:
            st.error("Username already exists") 