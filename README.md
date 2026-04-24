# 📚 Local RAG-Based Question Answering System

This project is a **Retrieval-Augmented Generation (RAG)** application built using **LangChain, Ollama, FAISS, and Streamlit**.

It allows users to upload **PDF or TXT files** and ask questions based on the document content.

---

## 🚀 Features

* 📄 Upload PDF or TXT documents
* 🔍 Semantic search using FAISS vector database
* 🤖 Local LLM (Mistral via Ollama)
* 💬 Ask questions and get contextual answers
* ⚡ Fast and fully offline (no API key required)

---

## 🛠️ Tech Stack

* Streamlit (UI)
* LangChain
* Ollama (Local LLM)
* FAISS (Vector Store)
* Python

---

## 📂 Project Structure

```
├── app.py              # Streamlit UI
├── rag_pipeline.py     # RAG logic
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/rag-app.git
cd rag-app
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Install Ollama

Download from: https://ollama.com

Then run:

```
ollama pull mistral
```

---

### 5. Run the App

```
streamlit run app.py
```

---

## 🧠 How It Works

1. Upload document
2. Text is split into chunks
3. Embeddings are created using Ollama
4. Stored in FAISS vector database
5. Relevant chunks are retrieved
6. LLM generates answer based on context

---

## 📌 Future Improvements

* Add chat history
* Support multiple files
* Add UI enhancements
* Deploy on cloud

---

## 👨‍💻 Author

SHUBHANK MANHAS

---

⭐ If you like this project, give it a star!
