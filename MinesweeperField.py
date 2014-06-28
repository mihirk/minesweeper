from Cells import Cells
from Command import Command


class MinesweeperField:
    def __init__(self, number_of_rows=0, number_of_mines=0):
        self.number_of_mines = number_of_mines
        self.number_of_rows = number_of_rows
        self.validate()
        self.cells = Cells(self.number_of_rows, self.number_of_mines)
        self.game_on = True
        self.show()

    def show(self):
        self.game_on = (self.cells.open_cell_count() != len(self.cells) - self.number_of_mines)
        grid = []
        row = []
        for cell in self.cells:
            if len(row) < self.number_of_rows:
                row.append(cell)
            if len(row) == self.number_of_rows:
                grid.append(row)
                print ' '.join(map(lambda x: x.__str__(), row))
                row = []

    def validate(self):
        if self.number_of_rows * self.number_of_rows >= self.number_of_mines >= 0 and self.number_of_rows > 0:
            pass
        else:
            raise IOError("Invalid input")


def main():
    number_of_rows = input("Enter the number of rows - ")
    number_of_mines = input("Enter the number of mines - ")
    field = MinesweeperField(number_of_rows, number_of_mines)
    while field.game_on:
        user_input = raw_input('Enter command ')
        command = Command(user_input)
        field.cells = command.execute_command(field.cells)
        if not field.cells:
            print "You lost :P"
            exit(0)
        field.show()
    print "You Won"


if __name__ == "__main__":
    main()


