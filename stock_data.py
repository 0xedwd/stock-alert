import requests
from config import STOCK_ENDPOINT, STOCK_API_KEY, STOCK_NAME


def get_latest_stock_price():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    return data_list[:2]  # Return data for the last two days
