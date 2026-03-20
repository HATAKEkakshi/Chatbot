## Conversational Q&A Chatbot
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

## Streamlit UI
st.set_page_config(page_title="Jarvis")
st.header("Chill , The Conversational Chatbot")

groq_api_key = "ggsk_ACb7TfTvCOhos66wL5G3WGdyb3FYxkbZAJ844gqhsn397b4xJIMI"

chat = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

if 'flowmessage' not in st.session_state:
    st.session_state['flowmessage'] = [
        SystemMessage(content="You are a Girl health matter expert. Answer all health-related queries regarding girls' health.")
    ]

## Function to get response
def get_response(question):
    st.session_state['flowmessage'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessage'])
    st.session_state['flowmessage'].append(AIMessage(content=answer.content))
    return answer.content

input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

## Only call the model when button is clicked
if submit:
    if input_text.strip():
        response = get_response(input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please enter a question before submitting.")
