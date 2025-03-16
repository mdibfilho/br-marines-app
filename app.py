from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Warhammer Tacticus API Demo"

@app.route('/api/player')
def player_details():
    api_url = 'https://api.tacticusgame.com/api/v1/player'
    headers = {
        'accept': 'application/json',
        'X-API-KEY': os.environ.get('WARHAMMER_API_KEY')
    }

    response = requests.get(api_url, headers=headers)

   if response.status_code == 200:
            data = response.json()

            # Pick interesting details to display clearly
            player_info = {
                'username': data.get('username'),
                'rank': data.get('rank'),
                'level': data.get('level'),
                'xp': data.get('xp'),
                'guild': data.get('guild', {}).get('name', 'No Guild'),
                'power': data.get('power')
            }

            return jsonify(player_info)
        else:
            # Clearly inform of API errors
            return jsonify({
                'error': f'API Error: {response.status_code}',
                'message': response.json()
            }), response.status_code


if __name__ == "__main__":
    app.run(debug=True)
