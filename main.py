import streamlit as st
from PIL import Image
from joblib import load

uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Test image')

model = load('lrc_xray.joblib')
