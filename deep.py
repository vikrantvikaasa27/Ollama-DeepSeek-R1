import ollama
import streamlit as st

st.title('Ollama - DeepSeek R1 - 1.5b')
input_text = st.text_area("What you need to search?")
response = ollama.generate(model='deepseek-r1:1.5b',
prompt= input_text,)

if input_text:
    st.write(response['response'])