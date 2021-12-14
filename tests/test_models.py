from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pewpewpew import Game, configure_routes

app = Flask(__name__)
configure_routes(app)
client = app.test_client()

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/back_end_test"
db = SQLAlchemy(app)
db.session.query(Game).delete()
db.session.commit()
db.session.close()
