import google.generativeai as g
import os
from dotenv import load_dotenv as l,find_dotenv as f


def get_my_key():
    l(f(),override=True)
    key=os.environ.get('GOOGLE_API_KEY')
    return key




