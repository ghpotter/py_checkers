class Player:
    """
    Basic Player class
    """
    def __init__(self, board):
        self.pos = (0, 0)
        self.color = 0
        board.grid[self.pos].player = self
    
    def move(self, dx, dy):
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        return [(self.pos[0] - dx, self.pos[1] - dy), self.pos]

    def change_color(self, color_array):
        self.color = (self.color + 1) % len(color_array)
        return color_array[self.color]
        