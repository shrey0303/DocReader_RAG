import logging
import time
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

def evaluate():
    """
    Dummy evaluation for retrieval+rerank pipeline.
    """
    queries = ["What is AI?", "Define ML"]
    ground_truth = [["chunk1"], ["chunk2"]]
    retrieved = [["chunk1", "chunk3", "chunk2"], ["chunk2", "chunk4", "chunk5"]]
    latencies = [0.12, 0.15]

    mrr = sum(1/(retrieved[i].index(gt[0])+1) if gt[0] in retrieved[i][:3] else 0 for i, gt in enumerate(ground_truth)) / len(queries)
    precision = sum(1 if gt[0] in retrieved[i][:3] else 0 for i, gt in enumerate(ground_truth)) / len(queries)

    logging.info(f"MRR@3: {mrr:.2f}, Precision@3: {precision:.2f}")
    print(f"MRR@3: {mrr:.2f}, Precision@3: {precision:.2f}")
    print(f"Avg latency: {sum(latencies)/len(latencies):.2f}s")

    plt.bar(["MRR@3", "Precision@3"], [mrr, precision])
    plt.title("Retrieval Metrics")
    plt.show()

if __name__ == "__main__":
    evaluate() 