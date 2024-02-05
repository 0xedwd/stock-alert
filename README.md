# Stock Price Alert Application

## Overview

Monitors stock price changes for a specific company (e.g., Apple Inc.) 
and sends SMS alerts if significant price changes are detected within a day. It utilizes the Alpha 
Vantage API for stock data and the News API to fetch relevant news articles related to the company. 
SMS notifications are sent via Twilio.

## Features
- Monitors stock price changes on a daily basis.


- Fetches relevant news articles if significant stock price changes are detected.


- Sends SMS alerts with stock price changes and news headlines.

## Prerequisites

- API keys for Alpha Vantage, News API, and Twilio.
- A Twilio verified phone number to send SMS alerts.

## Installation
1. Clone the repository.
2. Install required packages
3. Ensure environment variables are set.
4. Set up the configuration.

## Running the Application

Run the following command to start the application:

```bash
python3 main.py
```
## Customization

You can monitor different stocks or change the threshold for price change alerts by modifying the following variables in the code:

- STOCK_NAME: Set to the stock symbol you wish to monitor.


- COMPANY_NAME: The name of the company for fetching relevant news.


- THRESH_HOLD: The percentage change that triggers an alert.

## Reference Docs

- https://www.alphavantage.co/documentation
- https://newsapi.org/docs/endpoints/everything
- https://www.twilio.com/docs/messaging/quickstart
