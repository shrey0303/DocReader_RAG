import pytest
from rerank.reranker import Reranker

def test_rerank(monkeypatch):
    reranker = Reranker()
    def dummy_predict(pairs):
        return [0.2, 0.9, 0.5]
    monkeypatch.setattr(reranker.model, "predict", dummy_predict)
    candidates = ["a", "b", "c"]
    ranked = reranker.rerank("query", candidates, top_n=2)
    assert ranked[0][0] == "b"
    assert len(ranked) == 2 