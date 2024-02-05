from twilio.rest import Client
from config import TWILIO_SID, TWILIO_AUTH, TWILIO_FROM, TWILIO_TO


def send_sms(message):
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
        body=message,
        from_=TWILIO_FROM,
        to=TWILIO_TO,
    )
    return message.sid
