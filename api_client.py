import requests
import logging

class CatFactClient:
    """Handles API communication for cat facts."""
    
    def __init__(self, url="https://catfact.ninja/fact", timeout=5):
        self.url = url
        self.timeout = timeout
        self.max_retries = 2
    
    def fetch_fact(self):
        """Fetch a cat fact with retry logic."""
        for attempt in range(self.max_retries):
            try:
                response = requests.get(self.url, timeout=self.timeout)
                response.raise_for_status()
                return response.json().get("fact", "No fact available")
            except requests.exceptions.Timeout:
                if attempt < self.max_retries - 1:
                    logging.warning(f"Timeout attempt {attempt + 1}, retrying...")
                    continue
                return "Request timed out. Please try again."
            except requests.exceptions.ConnectionError:
                return "No internet connection. Check your network."
            except Exception as e:
                logging.error(f"Error: {e}")
                return f"Error: {str(e)}"