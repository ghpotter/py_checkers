import pygame

class Tile():
    """
    Basic tile for pygame interaction
    """
    piece = None
    player = None

    def __init__(self, pos, width, height, border):
        self.border_surface = pygame.Surface((width, height))
        self.border_surface = self.border_surface.convert()
        self.width = width - 2 * border
        self.height = height - 2 * border
        self.surface = pygame.Surface((self.width, self.height))
        self.surface = self.surface.convert()
        self.color = (0, 0, 0)
        self.border_pos = pos
        self.pos = (pos[0] + border, pos[1] + border)

    def check_in_border(self, pos):
        if self.pos[0] > pos[0] or self.pos[0] + self.width < pos[0]:
            return False
        if self.pos[1] > pos[1] or self.pos[1] + self.height < pos[1]:
            return False
        return True
    
    def set_color(self, color):
        self.color = color
        self.surface.fill(color)
    
    def highlight(self, color):
        self.border_surface.fill(color)
