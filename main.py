import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np

IMG_SIZE = 227

class_list = {0: 'NORMAL', 1: 'PNEUMONIA'}

input = open('lrc_xray.pkl', 'rb')
model = pkl.load(input)

uploaded_file = st.file_uploader("Choose an image file", type=(['png', 'jpg', 'jpeg']))
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Test image')

    if st.button('Predict'):
        image = image.resize((IMG_SIZE*IMG_SIZE*3, 1))
        feature_vector = np.array(image)
        st.write(model)
        label = model.predict(feature_vector)
        st.write(class_list[label])
