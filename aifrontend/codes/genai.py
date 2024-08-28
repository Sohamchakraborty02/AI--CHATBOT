from obtained_key import get_my_key as g
import google.generativeai as genai

print('my key is',g())

def talk_to_me():
    genai.configure(api_key=g())