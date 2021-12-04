from flask import Flask
import json
from app.routes import configure_routes

def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b"Hello, World!"
    assert response.status_code == 200

def test_post_route_success():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/games'

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
