<div align="center">

# 🩺 AI Medical Chatbot (Production RAG)

[![CI](https://github.com/AdithbabuT/Ai-medical-chatbot/actions/workflows/ci.yml/badge.svg)](https://github.com/AdithbabuT/Ai-medical-chatbot/actions)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-green.svg)](https://python.langchain.com/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Store-orange.svg)](https://github.com/facebookresearch/faiss)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](Dockerfile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A production-ready Retrieval-Augmented Generation (RAG) conversational AI system built with LangChain, FAISS Vector Database, HuggingFace sentence-transformers, and Groq high-speed LLM inference.**

[Overview](#-overview) • [RAG Architecture](#-rag-architecture) • [Features](#-key-features) • [Quickstart](#-quickstart) • [Docker Deployment](#-docker-deployment) • [Testing](#-testing)

</div>

---

## 🌟 Overview

The **AI Medical Chatbot** provides accurate, context-grounded answers to medical queries by synthesizing information strictly from trusted clinical reference materials and guidelines. By combining local vector search with high-throughput cloud inference, the system prevents hallucinations while providing citation of source excerpts.

---

## 🏗️ RAG Architecture

```
[Clinical PDF Documents]
           │
           ▼
[Recursive Character Chunking (500 tokens, 50 overlap)]
           │
           ▼
[HuggingFace Embeddings (all-MiniLM-L6-v2)]
           │
           ▼
[FAISS Vector Store Index]
           │
           ▼ (Top-3 Relevant Chunks)
[User Query] ──> [Custom Strict Medical Prompt] ──> [Groq LLM (Llama-3/Mistral)]
                                                               │
                                                               ▼
                                                  [Grounded Response + Sources]
```

---

## ✨ Key Features

- **📚 Grounded Retrieval-Augmented Generation**: Prevents hallucination by constraining responses strictly to retrieved medical context.
- **⚡ High-Throughput Inference**: Integrates Groq LLM API for sub-second token generation.
- **🔍 Dense Vector Retrieval**: Uses Facebook AI Similarity Search (FAISS) and `sentence-transformers/all-MiniLM-L6-v2`.
- **💬 Streamlit Chat UI**: Responsive, session-managed conversational user interface.
- **🐳 Containerized & Cloud-Ready**: Fully dockerized with multi-platform HuggingFace Spaces compatibility.

---

## 🚀 Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/AdithbabuT/Ai-medical-chatbot.git
cd Ai-medical-chatbot
```

### 2. Configure Environment Variables
Create a `.env` file from template:
```bash
cp .env.example .env
```
Fill in your API keys in `.env`:
```ini
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Ingest Documents into Vector Store
Place medical documents into `data/` and index embeddings:
```bash
python utils/create_memory.py
```

### 5. Launch Streamlit Application
```bash
streamlit run app.py
```

---

## 🐳 Docker Deployment

### Build Docker Image
```bash
docker build -t ai-medical-chatbot .
```

### Run Container
```bash
docker run -p 7860:7860 -e GROQ_API_KEY=your_api_key ai-medical-chatbot
```
*Access the application at: `http://localhost:7860`*

---

## 📂 Repository Structure

```
Ai-medical-chatbot/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI pipeline
├── utils/
│   ├── connect_memory.py        # FAISS index connector & QA chain builder
│   └── create_memory.py         # PDF chunking & vector indexing pipeline
├── tests/
│   └── test_rag.py              # Automated unit tests
├── .env.example
├── .gitattributes
├── .gitignore
├── Dockerfile                   # Production container definition
├── LICENSE                      # MIT License
├── app.py                       # Streamlit interactive chat interface
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🧪 Testing

Run unit tests locally:
```bash
pytest tests/ -v
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
