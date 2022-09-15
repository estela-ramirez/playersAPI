from flask import Flask, request
from load_data import csv_to_json

app = Flask(__name__)

csvFilePath = '/Users/EstelaRamirez/Desktop/players_API/players.csv'
players_dict = csv_to_json(csvFilePath)


@app.route("/")
def home():
    return "API is running"

# handle empty data 

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

app.run(debug=True)