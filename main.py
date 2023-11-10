import streamlit as st
from PIL import Image

uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False)
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

    image = Image.open(uploaded_file.name)
    
    st.image(image, caption='Sunrise by the mountains')
