import math
import constants

class Score():
    def __init__(self):
        self.score = 0
        self.total_time = 0

    def add_time(self, delta_time):
        self.total_time += delta_time

    def add_score(self, points):
        self.score += points

    def get_score(self):
        temp_score = self.score
        return math.ceil(temp_score + self.total_time * constants.SCORE_TIME_BONUS)

    def get_total_time(self):
        return self.total_time

    def get_time_bonus(self):
        return math.ceil(self.total_time * constants.SCORE_TIME_BONUS)