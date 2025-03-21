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

        player = data.get('player', {})
        details = player.get('details', {})

        # Return ONLY name and powerLevel clearly:
        filtered_details = {
            "name": details.get('name'),
            "powerLevel": details.get('powerLevel')
        }

        return jsonify(filtered_details)
    else:
        return jsonify({"error": response.status_code, "details": response.text}), response.status_code


if __name__ == "__main__":
    app.run(debug=True)
