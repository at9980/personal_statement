# app.py

import streamlit as st
from functions import get_answer

st.title("🤖 자기소개서 평가 시스템")

if "messages" not in st.session_state:
    st.session_state.messages = []

# 채팅 기록 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 및 응답 처리
if prompt := st.chat_input("수행하고자 하는 자기소개서 평가를 입력하세요."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = f"Bot: {get_answer(prompt.strip())}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
