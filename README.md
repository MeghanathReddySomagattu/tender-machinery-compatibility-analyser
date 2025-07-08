# Tender Machinery Compatibility Analyzer (LLM + RAG + Flask)

This project is an interactive web tool designed to simplify the machinery procurement process for tender applicants. It utilizes a Retrieval-Augmented Generation (RAG) pipeline with a large language model (LLM) backend to analyze tender titles and rank compatible machines based on a custom corpus of machine specifications.

Built with:

* Flask (Python backend)
* LangChain (LLM orchestration)
* ChromaDB (vector storage for retrieval)
* HuggingFace sentence-transformers
* HeroUI + Tailwind CSS (Frontend styling)

---

## ✨ Features

* 🧠 AI-powered tender understanding
* 🔍 Top 3 machine recommendations with compatibility scores
* 📊 Score explanation and suitability analysis
* 🔧 Modal view for customization potential and upgrade needs
* 📈 Extendable architecture with your own machinery corpus

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MeghanathReddySomagattu/tender-machinery-compatibility-analyser.git
cd tender-analyzer
```

### 2. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate.ps1
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

Ensure the following Python packages are included in requirements.txt:

```
flask
langchain-groq
langchain-huggingface
langchain-chroma
chromadb
sentence-transformers
```

### 4. Prepare Vector Store

Make sure your Chroma vector database is populated and exists at ./db. You can populate it using:

```python
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(docs, embedding, persist_directory="./db")
```

### 5. Set API Key

Set your GROQ API key in your shell:

```bash
export GROQ_API_KEY=your_key_here   # Linux/Mac
set GROQ_API_KEY=your_key_here      # Windows cmd
$env:GROQ_API_KEY="your_key_here"   # PowerShell
```

---

## 🧪 Running the App

```bash
python app.py
```

Open your browser and go to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖼️ UI Overview

* Textbox for tender title
* “Analyze” button
* Machine list with scores
* “Details” button shows popup modal with:

  * Customization feasibility
  * Modification requirements
  * Cost implications
  * Limitations

---

## 🛠️ Project Structure

```
tender-analyzer/
│
├── app.py                  # Flask backend logic
├── requirements.txt
├── db/                     # Persisted ChromaDB vectorstore
├── templates/
│   ├── base.html           # HeroUI layout & navbar
│   └── index.html          # Input form and results
└── static/
    └── styles.css          # Tailwind or custom styles
```

---

## 📦 Deployment

To deploy:

* Host via Gunicorn + Nginx or use a cloud platform like Render, Railway, or Heroku
* Set GROQ\_API\_KEY as environment variable in production

---

## 📌 Future Improvements

* Upload full tender documents (PDF parsing)
* Add search filters to machine results
* Support multiple corpora (by industry or vertical)
* PDF export or report generation
* Admin dashboard to manage machine entries

---

## 🧑‍💻 Author

Built by S Meghanath Reddy
Contributions welcome!
