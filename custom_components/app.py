import streamlit as st
import streamlit.components.v1 as components

# Declare the component
carousel_component = components.declare_component("carousel", url="http://localhost:3000")

# Define slides data
slides = [
    {"type": "text", "content": "Welcome to Slide 1"},
    {"type": "image", "content": "https://blog.hootsuite.com/wp-content/uploads/2021/07/free-stock-photos-03-scaled.jpeg"},
    {"type": "image", "content": "https://www.istockphoto.com/resources/images/PhotoFTLP/1035146258.jpg"},  # Another example image URL
]

# Use the component with custom height, width, and slides
carousel_component(height="200px", width="90%", slides=slides)