import streamlit as st
import base64
import requests
from PIL import Image
import io

#title, heading, other text
st.title("Find My Space")
st.subheader("Using machine learning to provide a cost-effective and world-wide accessible solution to parking deficiency.")




#Model predicitons, file uploader

image = st.file_uploader(label="Upload an image",accept_multiple_files=False, help="Upload an image to classify them")
if image:
    #converting the image to bytes
    img = Image.open(image)

    #image to be predicted
    st.image(img, caption = "Image to be predicted")

    #converting the image to bytes
    buf = io.BytesIO()
    img.save(buf,format = 'JPEG')
    byte_im = buf.getvalue()

    #converting bytes to b64encoding
    payload = base64.b64encode(byte_im)

    #file details
    file_details = {
      "file name": image.name,
      "file type": image.type,
      "file size": image.size
    }


import requests
import base64

def get_prediction(image_data):
  url = 'https://askai.aiclub.world/ffe11679-a633-4f88-8659-a1990d65ccb8'
  r = requests.post(url, data=image_data)
  response = r.json()['predicted_label']
  print(response)
  return response
response = get_prediction(payload)
st.write("response")

st.markdown("This is a **{}** space.".format(response))