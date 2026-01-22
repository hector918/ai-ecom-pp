import requests

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="qwen3-vl:30b"):
        self.base_url = base_url
        self.model = model

    def chat(self, prompt: str) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        r = requests.post(url, json=payload, timeout=120)
        r.raise_for_status()
        return r.json()["response"]
