from app import app
from flask import request
import json


def configure_routes(app):
    @app.route('/')
    def hello_world():
        return "Hello, World!"

    @app.route('/games', methods=['POST'])
    def receive_post():
        headers = request.headers
        data_string = request.get_data()
        data = json.loads(data_string)

        request_id = data.get('request_id')
        payload = data.get('payload')

        if request_id and payload:
            return 'ok', 200
        else:
            return 'bad request', 400
