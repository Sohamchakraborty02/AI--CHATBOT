import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv,find_dotenv
st.set_page_config(page_title='Q&A DEMO BY SOUPARNA')

st.header('HELLO')
status=load_dotenv(find_dotenv(),override=True)
mykey=os.environ.get('GOOGLE_API_KEY')
st.write(status)
genai.configure(api_key=mykey)
for m in genai.list_models():
    print(m,name)

model=genai.GenerativeModel('gemini-1.5-flash-latest')
chat=model.start_chat(history=[])