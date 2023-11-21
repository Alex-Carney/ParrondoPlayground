import streamlit as st

import base64

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

encoded_image = get_base64_encoded_image('assets/background.png')


st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;  /* or 'contain' depending on your preference */
        background-position: center;  /* Adjust as needed */
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h1 style='text-align: center; color: white; font-style: italic; 
                text-shadow: 2px 2px 4px #000000; 
                background-color: rgba(0, 0, 0, 0.6); 
                padding: 10px;'>
    Parrondo's Playground
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align: center; color: white; font-style: italic; 
                text-shadow: 2px 2px 4px #000000; 
                background-color: rgba(0, 0, 0, 0.5); 
                padding: 5px;'>
    Built by Alex Carney, Gavin Burns, Turner Mullarkey
    </h4>
    """,
    unsafe_allow_html=True
)
