
# api_handler.py
import requests
import logging 
logging.basicConfig(level=logging.DEBUG,filename='quote.log',format='%(asctime)s -%(levelname)s -%(message)s')

def get_random_quote():
    """Fetches a random quote from the quotable.io API."""
    try:
        response = requests.get("https://dd-api.doubledigit-solutions.com/welcome-msg")
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        data = response.json()
        logging.debug( f"the Response data : {data}")
        msg = data['msg']
        thought = data['thought']
        logging.info(f" Message is : {msg}")
        return f'"{msg}" - {thought}'
        # return data
    except requests.exceptions.RequestException as e:
        logging.error("could not fetch API")
        return f"Error: Could not fetch a quote. Please check your internet connection. Details: {e}"