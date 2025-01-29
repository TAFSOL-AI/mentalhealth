import requests


class OllamaClient:
    def __init__(self, base_url="https://efdd-119-73-96-200.ngrok-free.app"):
        self.base_url = base_url

    def generate_response(self, messages, model_name, format=None):
        endpoint = f"{self.base_url}/generate_response"
        payload = {
            "messages": messages,
            "model_name": model_name
        }
        
        # Only add format if it's not None
        if format is not None:
            payload["format"] = format
        
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()
        return response.json()
