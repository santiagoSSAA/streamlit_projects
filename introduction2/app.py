import streamlit as st
import pandas as pd

st.write("Hello, *world!* :sunglasses:")
st.markdown("### Testing 1, 2, 3, testiiing")
st.header("Header testing")

st.divider()

st.code("a = 1234")
with st.echo():
    st.write("This code will be printed")

st.divider()

st.latex("\int a x² \,dx")
st.text("Hello world")

st.divider()

st.metric("My metric", 42, 2)
selected = st.checkbox("I agree")
color = st.color_picker("Pick a color")
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])

st.divider()

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
    
data = st.file_uploader("Upload something (maybe a csv)")
image = st.camera_input("Take a picture")

st.divider()

col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")

@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")

is_pop_up = st.checkbox("Pop up form")
if is_pop_up:
    email_form()
    
st.divider()

c = st.empty()
st.write("This will show last")
c.write("This will be replaced")