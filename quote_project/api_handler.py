
# api_handler.py
import requests

def get_random_quote():
    """Fetches a random quote from the quotable.io API."""
    try:
        response = requests.get("https://dd-api.doubledigit-solutions.com/welcome-msg")
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        data = response.json()
        msg = data['msg']
        thought = data['thought']
        return f'"{msg}" - {thought}'
        # return data
    except requests.exceptions.RequestException as e:
        return f"Error: Could not fetch a quote. Please check your internet connection. Details: {e}"