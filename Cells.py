from MineCell import MineCell
from NonMineCell import NonMineCell
from Position import Position


class Cells():
    def __init__(self, number_of_rows, number_of_mines):
        self.occupied_positions = []
        self.cells = []
        self.add_cells(number_of_rows * number_of_rows - number_of_mines, number_of_rows,
                       NonMineCell)
        self.add_cells(number_of_mines, number_of_rows, MineCell)
        self.cells = sorted(self.cells, key=lambda cell: cell.position)


    def add_cells(self, count, number_of_rows, cell_type):
        for cell in range(count):
            cell_position = Position.get_position(number_of_rows, self.occupied_positions)
            self.occupied_positions.append(cell_position)
            self.cells.append(cell_type(cell_position))

    def open_cell_count(self):
        return len(filter(lambda cell: cell.status.is_open(), self.cells))

    def __iter__(self):
        for cell in self.cells:
            yield cell

    def __len__(self):
        return len(self.cells)