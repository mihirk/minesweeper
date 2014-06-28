from Cell import Cell


class MineCell(Cell):
    def __init__(self, position=None):
        Cell.__init__(self, position)

    def is_mine(self):
        return True
