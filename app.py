#Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = apikey

# App Framework
st.title('Writer GPT Creator')
prompt = st.text_input('Plug in your propt here')

# Template
title_template = PromptTemplate(
	input_variables = ['topic'],
	template='write me a book title about {topic}'
)

script_template = PromptTemplate(
	input_variables = ['title'],
	template='write me a short story based on this title TITLE: {title}'
)

#Llm chains
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)
sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)

# Show stuff to the screen if there's a prompt
if prompt:
	response = sequential_chain.run(prompt)
	st.write(response)
