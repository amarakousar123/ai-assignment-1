import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

# Configure Groq client
client = Groq(api_key=api_key)

# App title
st.title("📚 Smart Study Buddy")

st.write("Ask questions about studies, programming, or any concept.")

# User input
user_question = st.text_input(
    "Enter your question:",
    placeholder="e.g., Explain Binary Search in simple words"
)

# Button
if st.button("Get Answer"):

    system_prompt = """
    You are a friendly study assistant.
    Explain topics in simple language for beginners.
    Keep answers short, clear, and easy to understand.
    """

    final_prompt = system_prompt + "\n\n" + user_question

    with st.spinner("Thinking..."):

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": final_prompt}
            ]
        )

    st.subheader("📖 AI Response")
    st.write(response.choices[0].message.content)
