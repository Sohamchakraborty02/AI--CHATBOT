#Q&A  CHATBOT
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv,find_dotenv
st.set_page_config(page_title='Q&A DEMO BY SOUPARNA')

st.header('HELLO')
status=load_dotenv(find_dotenv(),override=True)
mykey=os.environ.get('GOOGLE_API_KEY')
#st.write(status)
genai.configure(api_key=mykey)
model=genai.GenerativeModel('gemini-1.5-flash-latest')
chat=model.start_chat(history=[])

   
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

#intilization of streamlit

st.header('GENAI conversation APPLICATION')
# intialize session history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
input=st.text_input("input:",key="input")
submit=st.button("ask the question")

if submit and input:
    response=get_gemini_response(input)
    #add user query and response to session state chat history
    st.session_state['chat_history'].append(("you",input))
    st.subheader('the response is')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot',chunk.text))
st.subheader('the chat history is ')

for role,text in st.session_state['chat_history']:
    st.write(f"{role}  :  {text}")