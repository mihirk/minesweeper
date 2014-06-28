from Position import Position


class Command:
    def __init__(self, command):
        command = command.strip().replace(' ', '').split('(')
        self.action = command[0]
        try:
            command = command[1].replace(')', '').split(',')
            self.position = Position(int(command[0]), int(command[1]))
        except:
            raise IOError('Invalid Command')

    def execute_command(self, grid):
        for cell in grid:
            if cell.position == self.position:
                cell.status.set_status(self.action)
                if cell.status.is_open() and cell.is_mine():
                    return False
                return grid
        raise IOError("Invalid Coordinates")