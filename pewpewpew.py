from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_cors import CORS
import json
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

basedir = os.path.abspath(os.path.dirname(__file__))
if os.environ.get('DATABASE_URL') is None:
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/back_end_test"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vqsggxzqtfottl:c71674bbbb90622bac9ab4a9ee75cff11ce69881a26dae466227dbc265122c37@ec2-54-158-247-97.compute-1.amazonaws.com:5432/dcei9coo1i8eg1"

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
        return "PewPewPew Scoring API"

    @app.route('/api/v1/leaderboard', methods=['GET'])
    def get_leaderboard():
        games_array = Game.query.order_by(Game.score.desc()).limit(10).all()

        leaderboard_json = {
            "games": []
            }

        for x in games_array:
            leaderboard_json["games"].append({
                "id": x.id,
                "player_name": x.player_name,
                "score": x.score
            })

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
                if int(payload['time_lapsed']) < 10:
                    score += 50000
                elif int(payload['time_lapsed']) < 25:
                    score += 25000
                elif int(payload['time_lapsed']) < 45:
                    score += 10000
                if int(payload['moves_taken']) < 55:
                    score += 50000
                elif int(payload['moves_taken']) < 65:
                    score += 25000
                elif int(payload['moves_taken']) < 75:
                    score += 10000
                score += int(payload['hidden_items_found'])*10000
                return score
                

            game = Game(player_name = payload['player_name'], score = score_calculations())

            db.session.add(game)
            db.session.commit()

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

    @app.route('/api/v1/games/<id>', methods=['DELETE'])
    def delete_game(id):
        game = Game.query.get(id)

        db.session.delete(game)
        db.session.commit()

        return "Deleted game"

configure_routes(app)
