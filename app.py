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
        'X-API-KEY': os.environ.get('WARHAMMER_API_KEY'),
        'accept': 'application/json'
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.status_code, "details": response.text}), response.status_code

@app.route('/api/player/details')
def player_details():
    api_url = 'https://api.tacticusgame.com/api/v1/player'
    headers = {
        'X-API-KEY': os.environ.get('WARHAMMER_API_KEY'),
        'accept': 'application/json'
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        
        player_info = {
            'Name': response.player.details.name,
            'Level': response.player.details.name
        }            

        return jsonify(response.json())
    else:
        return jsonify({"error": response.status_code, "details": response.text}), response.status_code


if __name__ == "__main__":
    app.run(debug=True)
