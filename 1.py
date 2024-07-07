import streamlit as st
import google.generativeai as genai
from stability_ai import text2image
import cv2
import googletrans

api_key = "sk-BiBSvnKtbsCDY2zDtBXAY2N9PHTsrTNGE8L8ZqKsmYkoU0Ck"
engine_id = "stable-diffusion-v1-6"
filename_save = "image_out.jpg"

genai.configure(api_key="AIzaSyBbrm4LIICJQnsxl1MSr9VV-7sGwbzx-RA")
model = genai.GenerativeModel("gemini-pro")

st.title("เว็บแอพแต่งนิทานและสร้างภาพ")



prompt_story = st.text_input("ป้อนลักษณะนิทานที่ต้องการ: ", "แต่งนิทาน")

try:
  response_story = model.generate_content(prompt_story)
  st.text("นิทาน:")
  st.text(response_story.text)
except Exception as e:
  st.error("เกิดข้อผิดพลาดในการแต่งนิทาน: {}".format(e))



prompt_image = st.text_input("ป้อน prompt ภาษาไทยสำหรับภาพ: ")

style = st.selectbox("เลือกรูปแบบภาพ",
                    ("watercolor painting",
                     "cartoon line drawing",
                     "flat cartoon illustration",
                     "sticker",
                     "3d rendering",
                     "kid crayon drawing"))

if st.button("สร้างภาพ"):
  try:
    response_story = model.generate_content(prompt_story)
    st.text("นิทาน:")
    st.text(response_story.text)
    prompt_en = googletrans.Translator().translate(prompt_image, src='th', dest='en').text

   
    prompt = prompt_en + " , " + style

    
    st.text("Prompt: {}".format(prompt))

    text2image(api_key,engine_id,prompt,filename_save)

   
    img = cv2.imread(filename_save)
    st.image(img, channels="BGR")
  except Exception as e:
    st.error("เกิดข้อผิดพลาดในการสร้างภาพ: {}".format(e))
