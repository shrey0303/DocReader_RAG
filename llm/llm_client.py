import logging
from typing import List
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO)

TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
TOGETHER_MODEL = "deepseek-ai/DeepSeek-R1-0528-tput"


def call_llm_together(prompt: str) -> str:
    """
    Call Together.ai LLM API with the given prompt using the DeepSeek-R1-0528-tput model.
    """
    api_key = os.environ.get("TOGETHER_API_KEY")
    if not api_key:
        raise ValueError("TOGETHER_API_KEY environment variable not set.")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": TOGETHER_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that only uses the provided context."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 512,
        "top_p": 0.9
    }
    response = requests.post(TOGETHER_API_URL, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    answer = result["choices"][0]["message"]["content"]
    logging.info("Together.ai LLM (DeepSeek) generated answer.")
    return answer


class LLMClient:
    def __init__(self, model: str = TOGETHER_MODEL):
        self.model = model

    def generate(self, query: str, context_chunks: List[str]) -> str:
        """
        Call Together AI LLM with context and query using DeepSeek model.
        """
        prompt = "\n".join(context_chunks) + f"\n\nQuestion: {query}\nAnswer:"
        return call_llm_together(prompt) 