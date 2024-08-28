#Q&A  CHATBOT
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv,find_dotenv
st.set_page_config(page_title='Q&A DEMO')

st.header('HELLO')
status=load_dotenv(find_dotenv(),override=True)
mykey=os.environ.get('GOOGLE_API_KEY')
st.write(status)
genai.configure(api_key=mykey)
model=genai.GenerativeModel('Gemini 1.5 Flash')
chat=model.start_chat(history=[])

   
def get_gemini_response():
    chat.send_message(question,stream=True)
    return response

#intilization of streamlit

st.header('GENAI conversation APPLICATION')
# intialize session history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


    
input=st.text_input("input:",key="input")
submit=st.button("ask the question")

if submit:
    response=get_gemini_response(input)
    st.subheader("the response is ")
    st.write(response.text)