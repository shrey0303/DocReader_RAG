import logging
from typing import List
import pandas as pd

logging.basicConfig(level=logging.INFO)

def load_and_chunk_csv(path: str, text_columns: List[str], chunk_size: int = 500) -> List[str]:
    """
    Reads specified text columns from a CSV and splits into chunks.
    Args:
        path: Path to the CSV file.
        text_columns: List of column names to read.
        chunk_size: Number of characters per chunk.
    Returns:
        List of text chunks.
    """
    df = pd.read_csv(path)
    text = " ".join(df[col].astype(str).str.cat(sep=" ") for col in text_columns if col in df)
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    logging.info(f"Loaded {len(chunks)} chunks from {path}")
    return chunks 