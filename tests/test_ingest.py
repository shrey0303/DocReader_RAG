import pytest
from ingest import pdf_loader, pptx_loader, csv_loader

# These tests use dummy paths and should be replaced with real sample files for actual testing.
def test_pdf_loader(monkeypatch):
    def dummy_extract(path, chunk_size=500):
        return ["chunk1", "chunk2"]
    monkeypatch.setattr(pdf_loader, "load_and_chunk_pdf", dummy_extract)
    chunks = pdf_loader.load_and_chunk_pdf("dummy.pdf")
    assert len(chunks) == 2

def test_pptx_loader(monkeypatch):
    def dummy_extract(path, chunk_size=500):
        return ["chunk1"]
    monkeypatch.setattr(pptx_loader, "load_and_chunk_pptx", dummy_extract)
    chunks = pptx_loader.load_and_chunk_pptx("dummy.pptx")
    assert len(chunks) == 1

def test_csv_loader(monkeypatch):
    def dummy_extract(path, text_columns, chunk_size=500):
        return ["chunk1", "chunk2", "chunk3"]
    monkeypatch.setattr(csv_loader, "load_and_chunk_csv", dummy_extract)
    chunks = csv_loader.load_and_chunk_csv("dummy.csv", ["col1"]) 
    assert len(chunks) == 3 