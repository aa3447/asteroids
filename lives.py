import constants

class Lives():
    def __init__(self):
        self.lives = constants.PLAYER_LIVES
        self.live_multiplier = 1

    def add_life(self):
        self.lives += 1
        print("Live Gained!")
        print(f"Lives: {self.lives}")

    def lose_life(self):
        self.lives -= 1
        print("Live Lost!")
        print(f"Lives: {self.lives}")

    def score_extra_life(self, score):
        if score >= constants.EXTRA_LIFE_SCORE * self.live_multiplier and score != 0:
            print("Extra life!")
            self.live_multiplier += 1
            self.add_life()  

    def get_lives(self):
        return self.lives
    
    def is_alive(self):
        return self.lives > 0