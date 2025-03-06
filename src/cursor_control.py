from pynput.mouse import Controller

class CursorControl:
    def __init__(self):
        self.mouse = Controller()

    def move_cursor(self, x, y):
        self.mouse.position = (x, y)

    def click(self):
        self.mouse.click()
