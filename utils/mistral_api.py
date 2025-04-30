import requests

MISTRAL_API_KEY = "KmZZ8AJyMJ82U2W4g7JmcHE6GMFrupy9"

def mistral_ask(prompt):
    """
    Sends a prompt to Mistral API and returns the response.
    """
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "mistral-small",  # Or "mistral-medium" if you have access
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()['choices'][0]['message']['content']