import unittest
import requests

class PlayersApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/api"
    PLAYERS_URL = "{}/players/".format(API_URL)
    playerID = "aardsda01"
    invalidID = "yelloIce"

    PLAYER_OBJ = {
        "bats": "R", 
        "bbrefID": "aardsda01", 
        "birthCity": "Denver", 
        "birthCountry": "USA", 
        "birthDay": 27, 
        "birthMonth": 12, 
        "birthState": "CO", 
        "birthYear": 1981, 
        "deathCity": "", 
        "deathCountry": "", 
        "deathDay": "", 
        "deathMonth": "", 
        "deathState": "", 
        "deathYear": "", 
        "debut": "2004-04-06", 
        "finalGame": "2015-08-23", 
        "height": 75, 
        "nameFirst": "David", 
        "nameGiven": "David Allan", 
        "nameLast": "Aardsma", 
        "playerID": "aardsda01", 
        "retroID": "aardd001", 
        "throws": "R", 
        "weight": 215
    }

    UPDATED_WEIGHT_PLAYER_OBJ = {
        "bats": "R", 
        "bbrefID": "aardsda01", 
        "birthCity": "Denver", 
        "birthCountry": "USA", 
        "birthDay": 27, 
        "birthMonth": 12, 
        "birthState": "CO", 
        "birthYear": 1981, 
        "deathCity": "", 
        "deathCountry": "", 
        "deathDay": "", 
        "deathMonth": "", 
        "deathState": "", 
        "deathYear": "", 
        "debut": "2004-04-06", 
        "finalGame": "2015-08-23", 
        "height": 75, 
        "nameFirst": "David", 
        "nameGiven": "David Allan", 
        "nameLast": "Aardsma", 
        "playerID": "aardsda01", 
        "retroID": "aardd001", 
        "throws": "R", 
        "weight": 216
    }

    UPDATED_W_AND_H_PLAYER_OBJ = {
        "bats": "R", 
        "bbrefID": "aardsda01", 
        "birthCity": "Denver", 
        "birthCountry": "USA", 
        "birthDay": 27, 
        "birthMonth": 12, 
        "birthState": "CO", 
        "birthYear": 1981, 
        "deathCity": "", 
        "deathCountry": "", 
        "deathDay": "", 
        "deathMonth": "", 
        "deathState": "", 
        "deathYear": "", 
        "debut": "2004-04-06", 
        "finalGame": "2015-08-23", 
        "height": 76, 
        "nameFirst": "David", 
        "nameGiven": "David Allan", 
        "nameLast": "Aardsma", 
        "playerID": "aardsda01", 
        "retroID": "aardd001", 
        "throws": "R", 
        "weight": 216
    }

    def _get_player_url(self, playerID):
        return "{}/players/{}".format(PlayersApiTest.API_URL, playerID)

    def _get_weight_url(self, playerID):
        return "{}/players/{}/weight".format(PlayersApiTest.API_URL, playerID)

    def _get_height_url(self, playerID):
        return "{}/players/{}/height".format(PlayersApiTest.API_URL, playerID)

    # GET request to api/players to get a list of all players
    def test_1_get_all_players(self):
        print(PlayersApiTest.PLAYERS_URL)
        res = requests.get(PlayersApiTest.PLAYERS_URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)  # there is 1 player

    # GET request to api/players/<playerID> to get json object of player
    def test_2_get_player(self):
        res = requests.get(self._get_player_url(PlayersApiTest.playerID))
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(res.json(), PlayersApiTest.PLAYER_OBJ)  

    # PUT request to api/players/<playerID>/weight to increment player's weight by 1
    def test_3_increment_weight(self):
        res = requests.put(self._get_weight_url(PlayersApiTest.playerID))
        self.assertEqual(res.status_code, 200)

    # GET request to api/players/<playerID> to check player's weight was incremented by 1
    def test_4_check_new_weight(self):
        res = requests.get(self._get_player_url(PlayersApiTest.playerID))
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(res.json(), PlayersApiTest.UPDATED_WEIGHT_PLAYER_OBJ)

    # PUT request to api/players/<playerID>/height to increment player's height by 1
    def test_5_increment_height(self):
        res = requests.put(self._get_height_url(PlayersApiTest.playerID))
        self.assertEqual(res.status_code, 200)

    # GET request to api/players/<playerID> to check player's height was incremented by 1
    def test_6_check_new_height(self):
        res = requests.get(self._get_player_url(PlayersApiTest.playerID))
        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(res.json(), PlayersApiTest.UPDATED_W_AND_H_PLAYER_OBJ)

    # GET request to api/players/<playerID> with invalid playerID
    def test_7_get_invalid_player(self):
        res = requests.get(self._get_player_url(PlayersApiTest.invalidID))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json()["message"], "error: player not found in DB")

    # PUT request to api/players/<playerID>/weight with invalid playerID
    def test_8_invalid_increment_weight(self):
        res = requests.put(self._get_height_url(PlayersApiTest.invalidID))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json()["message"], "error: player not found in DB")

    # PUT request to api/players/<playerID>/height with invalid playerID
    def test_9_invalid_increment_height(self):
        res = requests.put(self._get_height_url(PlayersApiTest.invalidID))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.json()["message"], "error: player not found in DB")

if __name__ == '__main__':
    unittest.main()