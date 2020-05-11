import pygame

from piece import Piece
from player import Player
from tile import Tile

class Board:
    """
    Basic Board class
    """
    RED = (255, 0 , 0)
    ORANGE = (255, 127, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    INDINGO = (39, 0, 51)
    VIOLET = (139, 0, 255)
    WHITE = (255, 255, 255)

    COLOR_ARRAY = [RED, ORANGE, YELLOW, GREEN, BLUE, INDINGO, VIOLET]

    number_of_rows = 8
    number_of_columns = 8
    grid = {}
    def __init__(self, width, height, border, screen):
        for row in range(self.number_of_columns):
            x = row * width
            for column in range(self.number_of_rows):
                y = column * height
                self.grid[(row, column)] = Tile((x, y), width, height, border)
                if (row + column) % 2:
                    self.grid[(row, column)].set_color((0, 0, 0))
                else:
                    self.grid[(row, column)].set_color((255, 0, 0))
                screen.blit(self.grid[(row, column)].surface, self.grid[(row, column)].pos)
        
        for i in range(self.number_of_columns):
            self.place_piece(i, 0, width, height, border, screen, 'red', True)
            self.place_piece(i, self.number_of_columns - 2, width, height, border, screen, 'black', False)
    
    def place_piece(self, i, offset, width, height, border, screen, color, playable):
        temp_piece = Piece(i, (i-1)%2 + offset, width, height, border, color, playable)
        self.grid[temp_piece.pos].piece = temp_piece
        self.update_tile(temp_piece.pos, screen)

    def update_tile(self, pos, screen):
        if self.grid[pos].player:
            self.grid[pos].highlight(self.grid[pos].player.change_color(self.COLOR_ARRAY))
        else:
            self.grid[pos].highlight((255, 255, 255))
        screen.blit(self.grid[pos].border_surface, self.grid[pos].border_pos)
        screen.blit(self.grid[pos].surface, self.grid[pos].pos)
        if self.grid[pos].piece:
            screen.blit(self.grid[pos].piece.border_surface, self.grid[pos].pos)
    
    def move_piece(self, from_pos, to_pos):
        if from_pos != to_pos:
            if self.grid[to_pos].piece:
                if self.grid[to_pos].piece.playable:
                    return
            self.grid[to_pos].piece = self.grid[from_pos].piece
            self.grid[from_pos].piece = None
            self.grid[to_pos].piece.pos = to_pos
    
    def move_player(self, player, dx, dy):
        self.grid[player.pos].player = None
        player.pos = (player.pos[0] + dx, player.pos[1] + dy)
        self.grid[player.pos].player = player

    def check_legal_move(self, pos):
        if self.grid[pos].piece:
            return not self.grid[pos].piece.playable
        return True
    
