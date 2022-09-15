from flask import Flask, request
from load_data import csv_to_json
import os

app = Flask(__name__)

try:
    csvFilePath = 'players.csv'
    players_dict = csv_to_json(csvFilePath)
except FileNotFoundError:
    print("File name or path are incorrect")


@app.route("/")
def home():
    return "API is running"

# returns the list(dict) of all players
@app.route("/api/players/", methods=['GET'])
def movies():
    return players_dict

# returns a single player by it's ID
@app.route("/api/players/<playerID>", methods=['GET'])
def get_movie(playerID):
    if playerID in players_dict:
        return players_dict[playerID]
    else:
        return {"message": "error: player not found in DB"}, 404

# given player's ID, increments a player's weight by 1
# returns updated DB 
@app.route("/api/players/<playerID>/weight", methods=['PUT'])
def increase_weight(playerID):
    if playerID in players_dict:
        players_dict[playerID]['weight'] += 1
    else:
        return {"message": "error: player not found in DB"}, 404
    return players_dict

# given player's ID, increments a player's height by 1
# returns updated DB 
@app.route("/api/players/<playerID>/height", methods=['PUT'])
def increase_height(playerID):
    if playerID in players_dict:
        players_dict[playerID]['height'] += 1
    else:
        return {"message": "error: player not found in DB"}, 404
    return players_dict

# app.run(debug=True)
port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)