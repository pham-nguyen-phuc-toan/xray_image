import streamlit as st
from PIL import Image

uploaded_files = st.file_uploader("Choose an image file", accept_multiple_files=False)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

image = Image.open(uploaded_file.name)

st.image(image, caption='Sunrise by the mountains')
