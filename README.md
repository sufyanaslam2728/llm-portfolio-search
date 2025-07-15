# Project RAG Search API

A FastAPI-based semantic search API using Gemma (via Ollama) with Retrieval-Augmented Generation (RAG). It indexes project data from a JSON file and answers user queries by retrieving and summarizing relevant entries.

---

## 🚀 Features

- In-memory semantic search with `sentence-transformers`
- Query-answering with `gemma:2b` via Ollama
- Simple FastAPI endpoint `/search`

---

## 📁 Folder Structure

```
rag-project-search-api/
├── venv/                     ← Virtual environment folder (excluded from Git)
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── data_loader.py
│   ├── retriever.py
│   ├── llm_rag.py
│   └── portfolio.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

---

### 1. Clone the Repo

```bash
git clone https://github.com/sufyanaslam2728/llm-portfolio-search.git
cd llm-portfolio-search
```

---

### 2. Setup Python Environment

```
# Navigate to your project directory
cd rag-project-search-api

# Create virtual environment
python -m venv venv

# Activate it (Linux/macOS)
source venv/bin/activate

# On Windows
venv\Scripts\activate

pip install -r requirements.txt
```

---

### 3. Install Ollama & Pull Model

Install from: https://ollama.com/download

Then pull a model:

```
ollama pull gemma:2b
```

---

### 4. Run the Microservice

```
uvicorn app.main:app --reload

```
