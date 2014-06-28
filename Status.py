class Status:
    def __init__(self, status='HIDDEN'):
        self.status = status
        self.status_map = {'HIDDEN': 'X', 'OPEN': 'O', 'FLAG': 'F'}

    def set_status(self, command):
        for key in self.status_map.keys():
            if self.status_map[key].lower() == command.lower():
                self.status = key

    def is_open(self):
        return self.status == 'OPEN'

    def __str__(self):
        return self.status_map[self.status]