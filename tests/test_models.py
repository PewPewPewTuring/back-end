from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pewpewpew import Game, configure_routes

app = Flask(__name__)
configure_routes(app)
client = app.test_client()

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/back_end_test"
db = SQLAlchemy(app)

def test_game_attributes():
    assert Game.query.all()[0].player_name == "AAA"
    assert Game.query.all()[1].player_name == "BBB"
    assert Game.query.all()[0].score == 0
    assert Game.query.all()[1].score == 10000
