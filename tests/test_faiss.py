import pytest
import numpy as np
from db.faiss_index import FaissIndex

def test_faiss_index():
    dim = 4
    index = FaissIndex(dim)
    embeddings = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0]], dtype='float32')
    metas = [{"id": i} for i in range(3)]
    index.add(embeddings, metas)
    query = np.array([[1,0,0,0]], dtype='float32')
    results = index.search(query, top_k=2)
    assert results[0][2]["id"] == 0
    assert len(results) == 2 