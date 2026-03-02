# 🏥 AI Medical Chatbot (Production-Ready RAG System)

A production-grade Retrieval-Augmented Generation (RAG) Medical Chatbot built using LangChain, FAISS, Hugging Face embeddings, and Groq LLM.

This system delivers context-grounded medical responses by retrieving relevant document chunks from a FAISS vector database before invoking the LLM.

---

## 🚀 Live Demo

🔗 **Hugging Face Deployment**  
https://huggingface.co/spaces/Adithbabu/ai-medical-chatbot

---

## 🧠 System Architecture

User Query  
↓  
Hugging Face Embeddings  
↓  
FAISS Vector Similarity Search (Top-K Retrieval)  
↓  
Context Injection into LLM  
↓  
Groq (Mistral Instruct Model)  
↓  
Grounded Medical Response  

---

## 🛠 Tech Stack

- **LLM**: Groq (Mistral Instruct)
- **Framework**: LangChain
- **Vector Store**: FAISS
- **Embeddings**: sentence-transformers (Hugging Face)
- **Deployment**: Docker + Hugging Face Spaces
- **Vector Storage**: Hugging Face Dataset Repository
- **Security**: Environment Variables & Hugging Face Secrets

---

## 🔐 Security & Production Practices

- No hardcoded API keys
- Secrets managed through Hugging Face deployment settings
- Modular architecture separating retrieval and inference
- Docker-based reproducible deployment
- Externalized vector index (not stored in GitHub)

---

## 📂 Project Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── utils/
│   └── connect_memory.py
```

---

## ⚙️ Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AdithbabuT/Ai-medical-chatbot.git
cd Ai-medical-chatbot
```

### 2️⃣ Create a `.env` file

```
GROQ_API_KEY=your_groq_api_key_here
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the application

```
streamlit run app.py
```

---

## 🏗 Deployment Details

- FAISS index stored in Hugging Face Dataset repository
- Docker container deployment
- Hosted via Hugging Face Spaces (CPU environment)
- Secure API key management via environment variables

---

## 📌 Key Features

- Context-aware RAG pipeline
- Controlled hallucination via strict prompt template
- Top-K semantic retrieval
- Secure API handling
- Production-ready modular design

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Adith Babu T**  
MSc Computer Science (AI / ML & Data Science)  
Bengaluru, India
