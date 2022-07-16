import pygame

WIDTH, HEIGHT = 720, 720
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
FPS = 60
#rgb
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
BROWN = (170,100,30)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

#Board

class Board:
	def __init__(self):
		self.board = [[]]
		self.selected_piece = None
		self.red_left = self.white_left = 12
		self.red_kings = self.white_kings = 0

	def draw_squares(self, win):
		win.fill(BLACK)
		for row in range(ROWS):
			for col in range(row % 2, ROWS, 2):
				pygame.draw.rect(win, BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))




class Piece:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        if colour == WHITE:
            self.direction = 1
        else:
            self.direction = -1
        self.x = 0
        self.y = 0

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2




def main():
	run = True
	clock = pygame.time.Clock()
	board = Board()

	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		board.draw_squares(WIN)
		pygame.display.update()
main()