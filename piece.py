import pygame

class Piece:
    """
    Basic Mobile Class
    """

    def __init__(self, x, y, width, height, border, color, playable):
        blue = (0, 0, 255)
        self.pos = (x, y)
        width -= 2 * border
        height -= 2 * border
        self.border_surface = pygame.Surface((width, height))
        self.border_surface = self.border_surface.convert()
        self.border_surface.fill(blue)
        self.border_surface.set_colorkey(blue)
        self.color = (230, 25, 25) if color == 'red' else (25, 25, 25)
        self.playable = playable
        center = (int(width/2), int(height/2))
        radius = int((height - 2)/2)
        pygame.draw.circle(self.border_surface, (255, 255, 255), center, radius, 2)
        pygame.draw.circle(self.border_surface, self.color, center, radius - 2)
    
    def move(self, dx, dy):
        self.pos = (self.pos[0] + dx,  self.pos[1] + dy)
        return [(self.pos[0] - dx, self.pos[1] - dy), self.pos]