from flask import Flask, request
# from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
import json
import psycopg2

app = Flask(__name__)
# app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/back_end_development"

conn = psycopg2.connect(
    host="localhost",
    database="back_end_development",
    user="postgres",
    password="pewpewpewturing")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
seeder = FlaskSeeder()
seeder.init_app(app, db)

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(64))
    score = db.Column(db.Integer)

def configure_routes(app):
    @app.route('/', methods=['GET'])
    def hello_world():
        return "Hello, World!"

    @app.route('/api/v1/leaderboard', methods=['GET'])
    def get_leaderboard():
        # import code; code.interact(local=dict(globals(), **locals()))
        games_array = Game.query.order_by(Game.score.desc()).limit(10).all()
        leaderboard_json = {
            "games": [
                    {
                    "id": games_array[0].id,
                    "player_name": games_array[0].player_name,
                    "score": games_array[0].score
                },
                {
                    "id": games_array[1].id,
                    "player_name": games_array[1].player_name,
                    "score": games_array[1].score
                },
                {
                    "id": games_array[2].id,
                    "player_name": games_array[2].player_name,
                    "score": games_array[2].score
                },
                {
                    "id": games_array[3].id,
                    "player_name": games_array[3].player_name,
                    "score": games_array[3].score
                },
                {
                    "id": games_array[4].id,
                    "player_name": games_array[4].player_name,
                    "score": games_array[4].score
                },
                {
                    "id": games_array[5].id,
                    "player_name": games_array[5].player_name,
                    "score": games_array[5].score
                },
                {
                    "id": games_array[6].id,
                    "player_name": games_array[6].player_name,
                    "score": games_array[6].score
                },
                {
                    "id": games_array[7].id,
                    "player_name": games_array[7].player_name,
                    "score": games_array[7].score
                },
                {
                    "id": games_array[8].id,
                    "player_name": games_array[8].player_name,
                    "score": games_array[8].score
                },
                {
                    "id": games_array[9].id,
                    "player_name": games_array[9].player_name,
                    "score": games_array[9].score
                }
            ]
        }

        response = app.response_class(
            response=json.dumps(leaderboard_json),
            status=200,
            mimetype="application/json"
        )

        return response

    @app.route('/api/v1/games', methods=['POST'])
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

configure_routes(app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
