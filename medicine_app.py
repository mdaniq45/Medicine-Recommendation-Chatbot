
import streamlit as st
from transformers import pipeline

# Load Hugging Face model
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

model = load_model()

# Streamlit UI
st.title("Medicine Recommendation Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Describe your symptoms..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate response
    with st.chat_message("assistant"):
        response = model(f"Suggest medicine for: {user_input}")
        medicine_recommendation = response[0]['generated_text']
        st.markdown(medicine_recommendation)
    
    st.session_state.messages.append({"role": "assistant", "content": medicine_recommendation})
