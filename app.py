import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from PyPDF2 import PdfReader
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("PDF Chatbot")

uploaded_file = st.file_uploader("Upload your PDF", type= "pdf")

def get_pdf_text(file):
    reader = PdfReader(file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    return text

if uploaded_file:
    pdf_text = get_pdf_text(uploaded_file)
    
    user_question = st.text_input("Ask a question about the PDF")
    
    if user_question:
        prompt = f"""
        Answer the question based ONLY on this document:
        {pdf_text}
        Question: {user_question}
        """

        response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
        )
        
        answer=response.choices[0].message.content
        st.write(answer)