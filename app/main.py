from flask import Flask, jsonify
import requests
import threading
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

# Background thread to send messages every 120 seconds
def message_scheduler():
    while True:
        send_message()
        time.sleep(120)

# Start the background thread
thread = threading.Thread(target=message_scheduler, daemon=True)
thread.start()

# Flask app setup
app = Flask(__name__)

@app.route('/send', methods=['GET'])
def trigger_message():
    send_message()
    return jsonify({'status': 'Message sent manually'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
