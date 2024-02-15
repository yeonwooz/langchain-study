#Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

# App Framework
st.title('Youtube GPT Creator')
prompt = st.text_input('Plug in your propt here')
