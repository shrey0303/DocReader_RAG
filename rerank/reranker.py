import logging
from typing import List, Tuple
from sentence_transformers import CrossEncoder

logging.basicConfig(level=logging.INFO)

class Reranker:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)
        logging.info(f"Loaded CrossEncoder model: {model_name}")

    def rerank(self, query: str, candidates: List[str], top_n: int = 3) -> List[Tuple[str, float]]:
        """
        Rerank candidates for a query.
        Returns: List of (text, score) sorted by score desc.
        """
        pairs = [[query, c] for c in candidates]
        scores = self.model.predict(pairs)
        ranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)[:top_n]
        logging.info(f"Reranked {len(candidates)} candidates.")
        return ranked 