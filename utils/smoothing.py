class Smoothing:
    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.prev_x, self.prev_y = None, None

    def smooth(self, x, y):
        if self.prev_x is None:
            self.prev_x, self.prev_y = x, y
        x = self.alpha * x + (1 - self.alpha) * self.prev_x
        y = self.alpha * y + (1 - self.alpha) * self.prev_y
        return int(x), int(y)
