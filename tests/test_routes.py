from flask import Flask
import json
from pewpewpew import app, configure_routes

app = Flask(__name__)
configure_routes(app)
client = app.test_client()

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
