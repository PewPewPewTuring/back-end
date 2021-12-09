from flask_seeder import Seeder
from pewpewpew import Game

class DemoSeeder(Seeder):
    def run(self):
        print("seeding ten games...")
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
        self.db.session.add(game01)
        self.db.session.add(game02)
        self.db.session.add(game03)
        self.db.session.add(game04)
        self.db.session.add(game05)
        self.db.session.add(game06)
        self.db.session.add(game07)
        self.db.session.add(game08)
        self.db.session.add(game09)
        self.db.session.add(game10)
        print("seeding completed!")
