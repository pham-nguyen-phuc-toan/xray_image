import streamlit as st
from PIL import Image
import pickle

IMG_SIZE = 227

pickle_in = open('lrc_xray.pkl', 'rb') 
model = pickle.load(pickle_in)

uploaded_file = st.file_uploader("Choose an image file", type=(['png', 'jpg', 'jpeg']))
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Test image')

    if st.button('Predict'):
        image = image.resize((1, IMG_SIZE*IMG_SIZE*3))
        st.write(model.predict(image))
