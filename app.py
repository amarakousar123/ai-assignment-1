import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Project Title
st.title("Smart Learning Companion")

st.write("Get quick and simple explanations for your academic questions.")

# User Input
question = st.text_input("Type your question here:")

# Submit Button
if st.button("Get Answer"):

    system_prompt = """
    You are an intelligent learning assistant.
    Explain concepts in easy and beginner-friendly language.
    Keep answers short, accurate, and easy to understand.
    """

    prompt = system_prompt + "\n\nQuestion: " + question

    response = model.generate_content(prompt)

    st.subheader("Response")

    st.write(response.text)