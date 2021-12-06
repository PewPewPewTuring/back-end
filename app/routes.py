from flask import request
from app.models import Game
import json

def configure_routes(app):
    @app.route('/')
    def hello_world():
        return "Hello, World!"

    @app.route('/games', methods=['POST'])
    def receive_post():
        data_string = request.get_data()
        data = json.loads(data_string)

        payload = data.get('payload')

        if payload:
            def score_calculations():
                score = 100000
                if int(payload['time_lapsed']) < 60:
                    score += 50000
                elif int(payload['time_lapsed']) < 120:
                    score += 25000
                elif int(payload['time_lapsed']) < 180:
                    score += 10000
                if int(payload['moves_taken']) < 50:
                    score += 50000
                elif int(payload['moves_taken']) < 75:
                    score += 25000
                elif int(payload['moves_taken']) < 100:
                    score += 10000
                score += int(payload['hidden_items_found'])*10000
                return score

            game = Game(player_name = payload['player_name'], score = score_calculations())

            game_json = {
            "player_name": game.player_name,
            "score": game.score
            }

            response = app.response_class(
                response=json.dumps(game_json),
                status=200,
                mimetype="application/json"
            )
            return response
        else:
            return 'bad request', 400
