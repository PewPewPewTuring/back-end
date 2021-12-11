from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from pewpewpew import configure_routes, Game

app = Flask(__name__)
configure_routes(app)
client = app.test_client()

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/back_end_test"
db = SQLAlchemy(app)
db.session.close()
db.drop_all()
db.create_all()
game01 = Game(player_name="AAA", score=0)
game02 = Game(player_name="AAA", score=10000)
game03 = Game(player_name="AAA", score=20000)
game04 = Game(player_name="AAA", score=30000)
game05 = Game(player_name="AAA", score=70000)
game06 = Game(player_name="AAA", score=50000)
game07 = Game(player_name="AAA", score=40000)
game08 = Game(player_name="AAA", score=80000)
game09 = Game(player_name="AAA", score=90000)
game10 = Game(player_name="AAA", score=60000)
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

def test_base_route():
    url = '/'

    response = client.get(url)
    assert response.get_data() == b"Hello, World!"
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
