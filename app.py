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
    headers = {'Authorization': f"Bearer {os.environ.get('WARHAMMER_API_KEY')}"}

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
