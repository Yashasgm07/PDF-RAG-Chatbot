# 📄 PDF Chatbot using RAG (GenAI Project)

## 🚀 Overview
This project is a **GenAI-powered PDF chatbot** that allows users to upload multiple documents and ask questions using **Retrieval-Augmented Generation (RAG)**.

It extracts text from PDFs, converts them into embeddings, stores them in a vector database (FAISS), and uses an LLM (via Groq API) to generate accurate, context-aware responses.

---

## 🧠 Key Features

- 📂 Upload and process multiple PDFs
- 🔍 Semantic search using FAISS vector database
- ⚡ Fast responses using Groq (LLaMA 3.1)
- 🧠 Context-aware answers using RAG pipeline
- 📚 Source attribution (shows where answer came from)
- 💬 Chat interface (ChatGPT-style UI)
- 🧹 Clear chat functionality
- 📥 Download chat history
- 🔄 Persistent vector database (no reprocessing needed)

---

## ⚙️ Tech Stack

- **Python**
- **LangChain**
- **FAISS (Vector Database)**
- **HuggingFace Embeddings**
- **Groq API (LLaMA 3.1)**
- **Streamlit (Frontend UI)**

---

## 🏗️ System Architecture


User Query
↓
FAISS Vector Search (Top-K Retrieval)
↓
Relevant Document Chunks
↓
LLM (Groq - LLaMA 3.1)
↓
Context-aware Answer


---

## 📂 Project Structure


PDF_RAG_Chatbot/
│── app/
│ ├── main.py # Streamlit UI
│ ├── pdf_processor.py # PDF parsing + chunking
│ ├── vector_store.py # FAISS DB creation/loading
│ ├── rag_pipeline.py # RAG logic + LLM integration
│
│── data/
│ ├── raw/ # Uploaded PDFs
│ ├── db/ # Saved vector DB
│
│── config/
│ └── settings.py # Configs (model, chunk size)
│
│── .env # API keys (not pushed)
│── requirements.txt
│── README.md


---

## 🧪 How It Works

1. Upload PDFs from the sidebar  
2. Text is extracted and split into chunks  
3. Chunks are converted into embeddings  
4. Stored in FAISS vector database  
5. User asks a question  
6. Relevant chunks are retrieved  
7. LLM generates answer based on context  

---

## 🖥️ Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/PDF-RAG-Chatbot.git
cd PDF-RAG-Chatbot
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Add Environment Variables

Create a .env file in root:

GROQ_API_KEY=your_api_key_here
5. Run Application
streamlit run app/main.py
📸 Demo

Add screenshots here (UI, chat, multi-PDF upload)

🚧 Challenges & Improvements
Challenges Faced
Handling multi-document retrieval
Preventing LLM hallucinations
Optimizing response speed
Designing clean UI for usability
Improvements Made
Increased retrieval depth (Top-K tuning)
Structured context formatting
Strong prompt engineering
Multi-document reasoning support
🎯 Future Enhancements
🔄 Conversation memory (context-aware chat)
⚡ Streaming responses (typing effect)
🌐 Cloud deployment
📊 Document insights & analytics
🧾 Support for more file types (DOCX, TXT)
🧠 Key Learnings
Deep understanding of RAG architecture
Practical use of vector databases (FAISS)
Prompt engineering for LLM grounding
Handling real-world multi-document QA systems
Building end-to-end GenAI applications
📌 Resume Description

Developed a multi-document PDF chatbot using Retrieval-Augmented Generation (RAG) with FAISS-based vector search and HuggingFace embeddings. Integrated Groq’s LLaMA 3.1 for fast, context-aware responses and built a Streamlit-based chat interface with source attribution and export functionality.

👨‍💻 Author

Yashas G M
GitHub: https://github.com/Yashasgm07
