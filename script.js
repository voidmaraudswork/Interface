import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

def load_hub():
    # Read the files
    with open("index.html", "r") as f:
        html = f.read()
    with open("style.css", "r") as f:
        css = f.read()
    with open("script.js", "r") as f:
        js = f.read()

    # Inject CSS into the head and JS into the body
    full_code = html.replace(
        '<link rel="stylesheet" href="style.css">', 
        f'<style>{css}</style>'
    ).replace(
        '<script src="script.js"></script>', 
        f'<script>{js}</script>'
    )
    return full_code

# Display the Ultra Modern Hub
components.html(load_hub(), height=1000, scrolling=True)
