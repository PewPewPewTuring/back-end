from pewpewpew import db
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(64))
    score = db.Column(db.Integer, index=True)

    # def __repr__(self):
    #     return '<This Game for {}>'.format(self.player_name)
