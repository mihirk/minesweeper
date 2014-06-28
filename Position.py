import random


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def get_position(number_of_rows, occupied_positions):
        while True:
            random_position = Position(random.randint(1, number_of_rows), random.randint(1, number_of_rows))
            if random_position not in occupied_positions:
                return random_position

    def __cmp__(self, other):
        if self.x < other.x:
            return -1
        elif self.x == other.x and self.y <= other.y:
            return -1
        else:
            return 1