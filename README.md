# 📚 The Ultimate Doc Reader

AI-Powered Document Analysis with RAG Technology

---

## 🚀 Project Overview
A full-stack Retrieval-Augmented Generation (RAG) system for document Q&A and analysis. Supports PDF, PPTX, and CSV ingestion, chunking, vector search, reranking, and LLM-powered answers using Together AI (DeepSeek model, free tier). Built with Streamlit for a modern, interactive UI.

---

## 🏗️ Architecture
- **Ingestion:** Chunk PDF, PPTX, CSV files
- **Vector DB:** FAISS for fast similarity search
- **Rerank:** BERT CrossEncoder (optional, placeholder)
- **LLM:** Together AI DeepSeek model via API
- **UI:** Streamlit dashboard (dark mode by default)
- **Evaluation:** MRR@3, Precision@3, latency (see `evaluate/`)

---

## 🛠️ Environment Setup
1. **Clone the repo**
2. **Create a virtual environment (Python 3.11 recommended):**
   ```sh
   python -m venv rag_env
   rag_env\Scripts\activate  # Windows
   # or
   source rag_env/bin/activate  # macOS/Linux
   ```
3. **Install requirements:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Create a `.env` file in the project root:**
   ```env
   TOGETHER_API_KEY=your-together-ai-api-key-here
   ```
5. **(Optional) Set up Docker:**
   ```sh
   docker build -t rag-app .
   docker run -p 8501:8501 --env-file .env rag-app
   ```

---

## 🌐 Running the App
1. **Activate your environment** (if not already):
   ```sh
   rag_env\Scripts\activate  # Windows
   # or
   source rag_env/bin/activate  # macOS/Linux
   ```
2. **Run Streamlit:**
   ```sh
   streamlit run api/app.py
   ```
3. **Open [http://localhost:8501](http://localhost:8501) in your browser.**

---

## 📂 Features & Usage
- **Multi-file upload:** Upload multiple PDF, PPTX, or CSV files at once
- **Automatic chunking:** Each file is split into manageable text chunks
- **Top-k context:** Only the top-k (default 3) most relevant chunks are shown and sent to the LLM
- **Prompt transparency:** See exactly what context is sent to the LLM
- **LLM answers:** Uses Together AI's DeepSeek model (free tier)
- **Dark mode:** Enabled by default via `.streamlit/config.toml`
- **No chunk preview clutter:** Only top-k chunks and prompt are shown after query
- **Concurrent/multi-user safe:** Each upload uses a unique temp file, no overwrites
- **.env support:** API key is loaded securely from `.env` using `python-dotenv`

---

## 📝 .env Example
```
TOGETHER_API_KEY=your-together-ai-api-key-here
```

---

## 🧪 Testing & Evaluation
- **Run all tests:**
  ```sh
  pytest
  ```
- **Evaluate retrieval/rerank:**
  ```sh
  python evaluate/evaluate.py
  ```
- **CI:** GitHub Actions workflow in `.github/workflows/ci.yml`

---

## 🛠️ Troubleshooting
- **ModuleNotFoundError:** Make sure you activate your virtual environment and install all requirements.
- **API key issues:** Ensure `.env` exists and contains a valid Together AI API key.
- **File not found:** Only one user/session should upload a file at a time for best results, or use unique filenames (already implemented).
- **Dark mode not working:** Check `.streamlit/config.toml` for theme settings.

---

## 📊 Example Usage
1. Upload one or more PDF/PPTX/CSV files
2. Enter a question about the content
3. See the top-k chunks used as context and the exact prompt sent to the LLM
4. Get an answer from the Together AI DeepSeek model

---

## 🏗️ Directory Structure
```
minimal-rag-model-main/
  ingest/         # PDF, PPTX, CSV loaders
  db/             # FAISS index logic
  rerank/         # Reranker logic (optional)
  llm/            # LLM client (Together AI)
  api/            # Streamlit app
  evaluate/       # Evaluation scripts
  tests/          # Pytest tests
  .streamlit/     # Streamlit config (dark mode)
  .env            # API key (not committed)
  requirements.txt
  Dockerfile
  README.md
```

---

## 📣 Credits & License
- Built by [Shrey](https://github.com/shrey0303)
- MIT License

---

**Enjoy your Ultimate Doc Reader!**






