import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini AI Chatbot", layout="centered")
st.title("🤖 Chatbot của tôi")

# Nhập API Key
api_key = st.sidebar.text_input("Nhập API Key của bạn:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Bạn muốn hỏi gì?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.info("Vui lòng nhập API Key ở thanh bên trái để bắt đầu.")
