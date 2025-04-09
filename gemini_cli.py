#!/usr/bin/env python3
import requests
import sys
from dotenv import load_dotenv
import os

load_dotenv(os.path.expanduser('~/llmcli/.env'))
API_KEY = os.getenv('GEMINI_API_KEY')

MODEL = "gemini-2.0-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

def query_gemini(prompt):
    system_instruction = (
        "Respond with only a 1–2 sentence plain explanation. "
        "Do not use any markdown or formatting. "
        "Do not include any code. Just explain the concept."
    )

    full_prompt = f"{system_instruction}\n\n{prompt}"
    print(f"[DEBUG] Sending prompt: '{prompt}'\n")

    response = requests.post(
        ENDPOINT,
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{
                "parts": [{"text": full_prompt}]
            }]
        }
    )

    try:
        data = response.json()
        output = data["candidates"][0]["content"]["parts"][0]["text"]
        print(f"[RESPONSE]\n{output}")
    except Exception as e:
        print(f"[ERROR] Malformed response: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: llm \"your question here\"")
    else:
        prompt = " ".join(sys.argv[1:])
        query_gemini(prompt)
