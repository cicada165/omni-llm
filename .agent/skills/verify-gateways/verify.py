import os
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor

MODELS = [
    "omni-1", 
    "omni-reasoning",
    "omni-creative",
    "omni-fast",
    "gpt-5.3-codex", 
    "claude-4-6-opus",
    "sonar-reasoning-pro", 
    "gemini-3-pro", 
    "llama-4-scout", 
    "mistral-large-3", 
    "kimi-k2-5"
]

BASE_URL = "http://localhost:4000/v1/chat/completions"
MASTER_KEY = "sk-1234"

def test_model(model):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Hi"}],
        "max_tokens": 10
    }
    headers = {
        "Authorization": f"Bearer {MASTER_KEY}",
        "Content-Type": "application/json"
    }
    
    start_time = time.time()
    try:
        response = requests.post(BASE_URL, json=payload, headers=headers, timeout=20)
        duration = time.time() - start_time
        
        if response.status_code == 200:
            return model, "PASS", f"{duration:.2f}s", ""
        else:
            return model, "FAIL", f"{duration:.2f}s", response.text[:100]
    except Exception as e:
        return model, "ERROR", "0.00s", str(e)

def main():
    print(f"{'MODEL':<25} {'STATUS':<10} {'LATENCY':<10} {'MESSAGE'}")
    print("-" * 60)

    # Cache Test: Run omni-1 again immediately
    print("\nVerifying Cache (Omni-1)...")
    _, success_status, latency, msg = test_model("omni-1")
    print(f"{'omni-1 (Cache)':<25} {success_status:<10} {latency}      {msg}")
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(test_model, MODELS)
        
        for model, status, latency, msg in results:
            print(f"{model:<25} {status:<10} {latency:<10} {msg}")

if __name__ == "__main__":
    main()
