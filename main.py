import pygame

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_SPACE

from board import Board
from piece import Piece
from player import Player
from tile import Tile

HEIGHT = 600
WIDTH = 800
BORDER = 4
CELLS_IN_ROW = 8
CELLS_IN_COLUMN = 8
cell_width = WIDTH / CELLS_IN_ROW
cell_height = HEIGHT / CELLS_IN_COLUMN

pygame.init()

pygame.key.set_repeat(100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
pygame.mouse.set_visible(1)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

screen.blit(background, (0, 0))
board = Board(cell_width, cell_height, BORDER, screen)

pygame.display.flip()

movement_queue = set()

player = Player(board)
selected_piece = None
allow_left_move = False
allow_right_move = False

running = True
last_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if selected_piece:
                if event.key == K_ESCAPE:
                    selected_piece = None
                elif event.key == K_LEFT:
                    if player.pos[0] > 1 and allow_left_move and board.check_legal_move((player.pos[0] - 2, player.pos[1])):
                        movement_queue.add(player.pos)
                        board.move_player(player, -2, 0)
                        allow_right_move = True
                        allow_left_move = False
                elif event.key == K_RIGHT:
                    if player.pos[0] < CELLS_IN_COLUMN - 2 and allow_right_move and board.check_legal_move((player.pos[0] + 2, player.pos[1])):
                        movement_queue.add(player.pos)
                        board.move_player(player, 2, 0)
                        allow_left_move = True
                        allow_right_move = False
                elif event.key == K_SPACE:
                    allow_left_move = False
                    allow_right_move = False
                    movement_queue.add(selected_piece.pos)
                    board.move_piece(selected_piece.pos, player.pos)
                    selected_piece = None
            else:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    if player.pos[1] > 0:
                        movement_queue.add(player.pos)
                        board.move_player(player, 0, -1)
                elif event.key == K_DOWN:
                    if player.pos[1] < CELLS_IN_COLUMN - 1:
                        movement_queue.add(player.pos)
                        board.move_player(player, 0, 1)
                elif event.key == K_LEFT:
                    if player.pos[0] > 0:
                        movement_queue.add(player.pos)
                        board.move_player(player, -1, 0)
                elif event.key == K_RIGHT:
                    if player.pos[0] < CELLS_IN_ROW - 1:
                        movement_queue.add(player.pos)
                        board.move_player(player, 1, 0)
                elif event.key == K_SPACE:
                    if board.grid[player.pos].piece:
                        if player.pos[1] < CELLS_IN_COLUMN - 1:
                            selected_piece = board.grid[player.pos].piece
                            if player.pos[0] == 0 and board.check_legal_move((player.pos[0] + 1, player.pos[1] + 1)):
                                movement_queue.add(player.pos)
                                board.move_player(player, 1, 1)
                            elif player.pos[0] < CELLS_IN_ROW - 1:
                                if board.check_legal_move((player.pos[0] - 1, player.pos[1] + 1)):
                                    movement_queue.add(selected_piece.pos)
                                    board.move_player(player, -1, 1)
                                    allow_right_move = True
                                elif board.check_legal_move((player.pos[0] + 1, player.pos[1] + 1)):
                                    movement_queue.add(selected_piece.pos)
                                    board.move_player(player, 1, 1)
                                    allow_left_move = True
                            elif player.pos[0] in (CELLS_IN_ROW - 2, CELLS_IN_ROW - 1) and board.check_legal_move((player.pos[0] - 1, player.pos[1] + 1)):
                                movement_queue.add(selected_piece.pos)
                                board.move_player(player, -1, 1)

    now = pygame.time.get_ticks()
    if now - last_time > 100:
        while len(movement_queue) > 0:
            board.update_tile(movement_queue.pop(), screen)
        board.update_tile(player.pos, screen)
        pygame.display.flip()
        last_time = now

