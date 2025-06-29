import logging
from typing import List
from PyPDF2 import PdfReader

logging.basicConfig(level=logging.INFO)

def load_and_chunk_pdf(path: str, chunk_size: int = 500) -> List[str]:
    """
    Reads a PDF file and splits its text into chunks.
    Args:
        path: Path to the PDF file.
        chunk_size: Number of characters per chunk.
    Returns:
        List of text chunks.
    """
    reader = PdfReader(path)
    text = " ".join(page.extract_text() or "" for page in reader.pages)
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    logging.info(f"Loaded {len(chunks)} chunks from {path}")
    return chunks 