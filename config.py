import os

# Company to track
STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"
THRESH_HOLD = 4

# API Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Twilio Phone Numbers
TWILIO_FROM = "YOUR_TWILIO_VERIFIED_NUMBER"
TWILIO_TO = "YOUR_PHONE_NUMBER"

# API Keys
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")


