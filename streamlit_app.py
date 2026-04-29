import streamlit as st
import streamlit.components.v1 as components

# Make sure the filename matches exactly what is in your GitHub repo
with open("index.html", "r") as f:
    html_code = f.read()

components.html(html_code, height=1000, scrolling=True)
