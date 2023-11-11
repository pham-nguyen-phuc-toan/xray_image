import streamlit as st
from PIL import Image

uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Test image')
