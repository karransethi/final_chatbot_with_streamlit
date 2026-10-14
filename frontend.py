import streamlit as st 
from langchain_core.messages import HumanMessage
from typing import List
from backend import workflow

if "messages" not in st.session_state :
    st.session_state['messages'] = []


user_input = st.chat_input('Type here')
thread_id = 1
if user_input :
    
    st.session_state['messages'].append({'role' : 'human', 'content' : user_input})
    config = {"configurable" : {"thread_id" : thread_id}}
    response = workflow.invoke({'messages' : HumanMessage(content=user_input)}, config=config)
    st.session_state['messages'].append({'role' : 'assistant', 'content' : response['messages'][-1].content})
    
    for msg in st.session_state['messages'] :
        with st.chat_message(msg['role']) : 
            st.text(msg['content'])
    