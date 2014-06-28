from Status import Status


class Cell(object):
    def __init__(self, position=None):
        self.status = Status()
        self.position = position

    def is_mine(self):
        return False

    def __str__(self):
        return self.status.__str__()