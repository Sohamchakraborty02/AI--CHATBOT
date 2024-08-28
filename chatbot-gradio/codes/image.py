#IMAGE  CHATBOT
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv,find_dotenv
st.set_page_config(page_title='IMAGE DEMO BY SOUPARNA')


status=load_dotenv(find_dotenv(),override=True)
mykey=os.environ.get('GOOGLE_API_KEY')
st.write(status)
genai.configure(api_key=mykey)
model=genai.GenerativeModel('gemini-1.5-flash-latest')
chat=model.start_chat(history=[])

   
def get_gemini_response_imagge(input,image):
    model=genai.GenerativeModel('gemini-1.5-flash-latest')
    if input!='':
        response=model.generate_content(input,image)
    else:
        response=model.generate_content(image)
    
    return response.text



st.subheader('HI GENAI!!')
input=st.text_input("input prompt",key="input")
u=st.file_uploader("choose an image..",type=['jpg','png','jpeg'])
image=""
if u is not None:
    image=image.open(u)
    st.image(image,caption="upload image",use_column_width=True)
submit=st.button("tell me somthing about image")   
if submit:
    response=get_gemini_response_imagge(input,image)
    st.subheader("the response is")
    st.write("response")