import logging
from typing import List, Tuple, Dict
import faiss
import numpy as np

logging.basicConfig(level=logging.INFO)

class FaissIndex:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []  # List[Dict]
        self.dim = dim

    def add(self, embeddings: np.ndarray, metadatas: List[Dict]):
        """
        Add embeddings and metadata to the index.
        """
        self.index.add(embeddings)
        self.metadata.extend(metadatas)
        logging.info(f"Added {len(embeddings)} vectors to index.")

    def search(self, query_emb: np.ndarray, top_k: int = 3) -> List[Tuple[int, float, Dict]]:
        """
        Search for top_k nearest neighbors.
        Returns: List of (index, score, metadata)
        """
        D, I = self.index.search(query_emb, top_k)
        results = [(int(idx), float(dist), self.metadata[int(idx)]) for idx, dist in zip(I[0], D[0])]
        return results 