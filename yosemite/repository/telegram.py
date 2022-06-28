import requests
import os

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_GROUP_ID')
MAX_CHAR_MESSAGE = int(os.environ.get('TELEGRAM_MAX_CHAR_MESSAGE', '2000'))


def send_message(text):
    while len(text) > 0:
        half_text = text[0:MAX_CHAR_MESSAGE]
        _send_message(half_text)
        text = text[MAX_CHAR_MESSAGE::]


def _send_message(text):
    url = "https://api.telegram.org/bot%s/sendMessage" % BOT_TOKEN
    body = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'markdown'
    }
    print("telegram: message sent! response=", requests.post(url, body).json())
