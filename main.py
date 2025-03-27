##conversional  q&a chatbot
import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_community.chat_models import ChatOpenAI
from langchain_groq import ChatGroq

##streamlit ui
st.set_page_config(page_title="Jarvis")
st.header("Jarvis , The Conversational Chatbot")
groq_api_key="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"
from dotenv import load_dotenv # type: ignore
load_dotenv()
import os
chat=ChatGroq(model="llama-3.3-70b-specdec",groq_api_key=groq_api_key)
if 'flowmessage' not in st.session_state:
    st.session_state['flowmessage']=[
        SystemMessage(content="You are Girl matter expert it means all health related query regarding girls healht ")
        ]
##function to load opeai 
def get_openai_response(question):
    st.session_state['flowmessage'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessage'])
    st.session_state['flowmessage'].append(AIMessage(content=answer.content))
    return answer


input=st.text_input("Input : ",key="input")
response=get_openai_response(input)
submit=st.button("Ask the question")
#if ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)