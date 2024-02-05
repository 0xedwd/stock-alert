import requests
from config import NEWS_ENDPOINT, NEWS_API_KEY, COMPANY_NAME


def get_company_news():
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"][:3]  # Get the first three articles
    return articles
