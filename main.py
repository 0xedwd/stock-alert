from stock_data import get_latest_stock_price
from news_data import get_company_news
from notification_service import send_sms
from config import STOCK_NAME, THRESH_HOLD


def check_stock_and_notify():
    # get latest stock price
    data_list = get_latest_stock_price()
    yesterday_data, day_before_yesterday_data = data_list
    yesterday_closing_price = float(yesterday_data["4. close"])
    day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
    difference = yesterday_closing_price - day_before_yesterday_closing_price
    diff_percent = round((difference / yesterday_closing_price) * 100)

    up_down = '🔺' if difference > 0 else '🔻'

    # check if diff meets threshold and send sms
    if abs(diff_percent) > THRESH_HOLD:
        articles = get_company_news()
        formatted_articles = [
            f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
            for article in articles]

        for article in formatted_articles:
            send_sms(article)


if __name__ == "__main__":
    check_stock_and_notify()
