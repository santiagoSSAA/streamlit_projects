import streamlit as st
x = st.slider('x') # this is a widget
st.write(x, 'squared is', x*x)
