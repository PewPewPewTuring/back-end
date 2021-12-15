from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from pewpewpew import configure_routes, Game, score_calculations

app = Flask(__name__)
configure_routes(app)
client = app.test_client()

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/back_end_test"
db = SQLAlchemy(app)
db.session.query(Game).delete()
db.session.commit()
game01 = Game(player_name="AAA", score=0)
game02 = Game(player_name="BBB", score=10000)
game03 = Game(player_name="CCC", score=20000)
game04 = Game(player_name="DDD", score=30000)
game05 = Game(player_name="EEE", score=70000)
game06 = Game(player_name="FFF", score=50000)
game07 = Game(player_name="GGG", score=40000)
game08 = Game(player_name="HHH", score=80000)
game09 = Game(player_name="III", score=90000)
game10 = Game(player_name="JJJ", score=60000)
db.session.add(game01)
db.session.add(game02)
db.session.add(game03)
db.session.add(game04)
db.session.add(game05)
db.session.add(game06)
db.session.add(game07)
db.session.add(game08)
db.session.add(game09)
db.session.add(game10)
db.session.commit()
db.session.close()

def test_base_route():
    url = '/'

    response = client.get(url)
    assert response.get_data() == b"PewPewPew Scoring API"
    assert response.status_code == 200

def test_post_route_success():
    url = '/api/v1/games'

    mock_request_data = {
        "payload": {
            "player_name": "AAA",
            "time_lapsed": "110",
            "moves_taken": "50",
            "hidden_items_found": "2"
        }
    }

    mock_game_response = {
        "player_name": "AAA",
        "score": 170000}

    response = client.post(url, data=json.dumps(mock_request_data))
    assert response.status_code == 200
    response_data_string = response.get_data()
    response_data = json.loads(response_data_string)
    assert response_data == mock_game_response

def test_get_route_leaderboard():
    url = '/api/v1/leaderboard'

    response = client.get(url)

    assert response.status_code == 200

    response_data_string = response.get_data()
    response_data = json.loads(response_data_string)

    assert type(response_data) == dict
    assert type(response_data['games']) is list
    assert len(response_data['games']) == 10
    assert type(response_data['games'][0]) is dict
    assert type(response_data['games'][0]['player_name']) is str
    assert type(response_data['games'][0]['score']) is int

def test_score_logic():
    payload01 = {
        "player_name": "AAA",
        "time_lapsed": "44",
        "moves_taken": "50",
        "hidden_items_found": "2"
    }
    assert score_calculations(payload01) == 180000

    payload02 = {
        "player_name": "AAA",
        "time_lapsed": "9",
        "moves_taken": "63",
        "hidden_items_found": "0"
    }

    assert score_calculations(payload02) == 175000

    payload03 = {
        "player_name": "AAA",
        "time_lapsed": "11",
        "moves_taken": "67",
        "hidden_items_found": "0"
    }

    assert score_calculations(payload03) == 135000

def test_delete_game():
    game_id = Game.query.all()[-1].id
    url = f"/api/v1/games/{game_id}"

    response = client.delete(url)

    assert Game.query.all()[-1].id != game_id

def test_get_all_games():
    url = '/api/v1/games'

    response = client.get(url)

    assert response.status_code == 200

    response_data_string = response.get_data()
    response_data = json.loads(response_data_string)

    assert type(response_data) == dict
    assert type(response_data['games']) is list
    assert type(response_data['games'][0]) is dict
    assert type(response_data['games'][0]['id']) is int  
    assert type(response_data['games'][0]['player_name']) is str
    assert type(response_data['games'][0]['score']) is int
