import streamlit as st
from PIL import Image
from joblib import load

IMG_SIZE = 227

model = load('lrc_xray.joblib')

uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Test image')

    if st.button('Predict'):
        image = image.reshape(1, IMG_SIZE*IMG_SIZE*3)
        st.write(model.predict(image))
