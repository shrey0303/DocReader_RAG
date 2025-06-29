import streamlit as st
import time
import logging
import sys
import os
import uuid
from datetime import datetime

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ingest import pdf_loader, pptx_loader, csv_loader

logging.basicConfig(level=logging.INFO)

# Set page config
st.set_page_config(
    page_title="The Ultimate Doc Reader",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 The Ultimate Doc Reader")
st.markdown("### AI-Powered Document Analysis with RAG Technology")

uploaded_files = st.file_uploader(
    "Upload PDF, PPTX, or CSV (multiple files supported)",
    type=["pdf", "pptx", "csv"],
    accept_multiple_files=True
)
query = st.text_input("Enter your query:")

# Use session state to store chunks for each file
if 'file_chunks' not in st.session_state:
    st.session_state.file_chunks = {}

if uploaded_files:
    for uploaded_file in uploaded_files:
        filetype = uploaded_file.name.split(".")[-1].lower()
        unique_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        temp_filename = f"temp_{unique_id}_{timestamp}.{filetype}"
        with open(temp_filename, "wb") as f:
            f.write(uploaded_file.read())
        if filetype == "pdf":
            chunks = pdf_loader.load_and_chunk_pdf(temp_filename)
        elif filetype == "pptx":
            chunks = pptx_loader.load_and_chunk_pptx(temp_filename)
        elif filetype == "csv":
            import pandas as pd
            df = pd.read_csv(temp_filename)
            chunks = csv_loader.load_and_chunk_csv(temp_filename, list(df.columns))
        else:
            chunks = []
        st.session_state.file_chunks[uploaded_file.name] = chunks
        st.success(f"✅ File {uploaded_file.name} uploaded and chunked into {len(chunks)} chunks.")
        # Clean up temp file
        os.remove(temp_filename)

if query and st.session_state.file_chunks:
    start = time.time()
    # Combine all chunks from all files
    all_chunks = []
    for fname, chunks in st.session_state.file_chunks.items():
        all_chunks.extend(chunks)
    # Show only top-k chunks (k=3)
    k = 3
    top_chunks = all_chunks[:k]
    st.subheader(f"🎯 Top {k} Chunks Used as Context:")
    for i, chunk in enumerate(top_chunks):
        st.text_area(f"Top Chunk {i+1}", chunk, height=80, key=f"top_chunk_{i}")
    prompt = "\n".join(top_chunks) + f"\n\nQuestion: {query}\nAnswer:"
    st.subheader("🤖 Prompt Sent to LLM:")
    st.code(prompt)
    st.write("\n💬 LLM Answer: This is a placeholder answer.")
    latency = time.time() - start
    st.write(f"⏱️ Retrieval + rerank latency: {latency:.2f} seconds") 