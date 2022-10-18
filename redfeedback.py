import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO


st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)

   
   
   
    if img_array.shape > (300,600,3):
        btn = st.download_button(
            label="Download image",
            data=img_file_buffer,
            file_name="correctiv_action.png",
            mime="image/png"
          )



