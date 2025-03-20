import requests
import time

# Replace with your Bot Token and Group Chat ID
BOT_TOKEN = '7474354923:AAFK9TeP53vQ6SzKBCJ7MU3OOocEuLBsT88'
GROUP_CHAT_ID = '-4765614301'
MESSAGE = 'Hello from your bot!'

# Telegram API URL
BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

def send_message():
    payload = {
        'chat_id': GROUP_CHAT_ID,
        'text': MESSAGE
    }
    response = requests.post(BASE_URL, data=payload)
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Failed to send message: {response.text}')

if __name__ == "__main__":
    while True:
        send_message()
        time.sleep(3)  # Wait for 3 seconds before sending the next message
