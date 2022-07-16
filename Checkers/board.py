import pygame
BLACK = (0,0,0)
ROWS, COLS = 8, 8
BROWN = (170,100,30)
SQUARE_SIZE = WIDTH//COLS

class Board:
	def __init__(self):
		self.board = [[]]
		self.selected_piece = None
		self.red_left = self.white_left = 12
		self.red_kings = self.white_kings = 0

	def draw_cubes(self, win):
		win.fill(BLACK)
		for row in range(ROWS):
			for col in range(row % 2, ROWS, 2):
				pygame.draw.rect(win, BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

