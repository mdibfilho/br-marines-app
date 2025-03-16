from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Warhammer Tacticus API Demo"

@app.route('/api')
def tactic_api():
    api_url = 'https://api.tacticusgame.com/api/v1/player'
    headers = {'Authorization': f"Bearer {os.environ.get('50aaf9c9-5d94-4036-89af-5f8b99c67161')}"}

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
