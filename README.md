# AI PDF Chatbot

An AI-powered web application that allows users to upload a PDF and ask questions based on its content.

---

## Features

* Upload any PDF document
* Extract text from the PDF
* Ask questions based on the document
* AI generates answers using LLaMA3 model via Groq API

---

## Tech Stack

* Python
* Streamlit (UI)
* PyPDF2 (PDF text extraction)
* Groq API (LLaMA3 model)

---

## Installation

```bash
pip install streamlit groq PyPDF2
```

---

## Run the App

```bash
streamlit run app.py
```

---

## How It Works

1. User uploads a PDF
2. Text is extracted using PyPDF2
3. User asks a question
4. Prompt is sent to Groq API
5. AI generates answer based on the document

---

## Limitations

* Sends full PDF text (not scalable for large documents)
* No context memory
* No vector database

---

## Future Improvements

* Implement RAG (Retrieval Augmented Generation)
* Use vector database (FAISS)
* Add chat history
* Support multiple PDFs

---

## Author

Ayush. Developed as an AI-powered application to demonstrate LLM integration, prompt engineering, and document-based question answering.
