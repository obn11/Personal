from random import randint
from random import shuffle
TLIST = ['Go','B1','Chest','B2','IT','T1','lB1','Chance','lB2','lB3',
         'Jail','P1','U1','P2','P3','T2','O1','Chest','O2','O3',
         'Free Parking','R1','Chance','R2','R3','T3','Y1','Y2','U2','Y3',
         'Go Jail','G1','G2','Chest','G3','T4','Chance','dB1','LT','dB2']
NUM_CHANCE_CARDS = 16
CHANCE_CARDS = ['Go','B3S','R3','TN','TN','T3','UN']
CHANCE_CARDS += ['dB2', 'P1']
NUM_CHEST_CARDS = 13
COMMUNITY_CARDS = ['Go','Jail']

class tile():

    def __init__(self, name, count=0):
        self.name = name
        self.count = count

    def __str__(self):
        strn = "{}: {}".format(self.name, self.count)
        return strn

    def __repr__(self):
        strn = "({}: {})".format(self.name, self.count)
        return strn

    def land(self, place, board, chance, chest):
        self.count += 1
        if self.name == 'Chance':
            place, board, chance, chest = draw_chance(place, board, chance, chest)
        if self.name == 'Chest':
            place, board, chance, chest = draw_chest(place, board, chance, chest)
        if self.name == 'Go Jail':
            position = 10
            board[10].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
        return place, board, chance, chest
    
    def add_avg(self, avg):
        self.count += avg


def draw_chance(place, board, chance, chest):
    if len(chance) == 0:
        chance, _ = init_decks()
    card = chance.pop()
    if card != 0:
        if card == 'Go':
            place = 0
            board[0].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
        elif card == 'B3S':
            place -= 3
            board[place].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
        elif card == 'R3':
            place = 24
            board[24].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
        elif card == 'T3':
            place = 25
            board[25].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
        elif card == 'TN':
            while place % 10 != 5:
                place = (place + 1) % 40
            board[place].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
        elif card == 'UN':
            while board[place].name[0] != 'U':
                place = (place + 1) % 40
            board[place].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
        elif card == 'dB2':
            place = 39
            board[39].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
        elif card == 'P1':
            place = 11
            board[11].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
    return place, board, chance, chest


def draw_chest(place, board, chance, chest):
    if len(chest) == 0:
        _, chest = init_decks()
    card = chest.pop()
    if card != 0:
        if card == 'Go':
            place = 0
            board[0].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
        if card == 'Jail':
            place = 10
            board[10].land(place, board, chance, chest)
            board[40].land(place, board, chance, chest)
    return place, board, chance, chest


def roll():
    "Rolls 2 d6s and returns the sum and true if they are the same"
    Double = False
    D1 = randint(1, 6)
    D2 = randint(1, 6)
    if D1 == D2:
        Double = True
    return (D1 + D2), Double


def init_board():
    board = [0] * 41
    for i in range(40):
        board[i] = tile(TLIST[i])
    board[40] = tile("total")
    return board


def init_decks():
    n_ch = NUM_CHANCE_CARDS
    n_co = NUM_CHEST_CARDS
    chance_d = [0] * n_ch
    chest_d = [0] * n_co
    for i, item in enumerate(CHANCE_CARDS):
        chance_d[i] = item
    for i, item in enumerate(COMMUNITY_CARDS):
        chest_d[i] = item
    shuffle(chance_d), shuffle(chest_d)
    return chance_d, chest_d


def take_turn(place, board, chance, chest):
    num, dub = roll()
    place = (place + num) % 40
    place, board, chance, chest = board[place].land(place, board, chance, chest)
    board[40].land(place, board, chance, chest)
    if dub:
        num, dub = roll()
        place = (place + num) % 40
        place, board, chance, chest = board[place].land(place, board, chance, chest)
        board[40].land(place, board, chance, chest)
        if dub:
            num, dub = roll()
            if dub:
                place = 10
                place, board, chance, chest = board[place].land(place, board, chance, chest)
                board[40].land(place, board, chance, chest)
            else:
                place = (place + num) % 40
                place, board, chance, chest = board[place].land(place, board, chance, chest)
                board[40].land(place, board, chance, chest)
    return place, board, chance, chest


def print_board(board):
    for i in board:
        print(i)


def print_board2(board):
    for i in board:
        strn = "{}: {:.2f}%".format(i.name, i.count)
        print(strn)


def print_by_street(board):
    print("Brown: {:.2f}".format(board[1].count + board[3].count))
    print("Light Blue: {:.2f}".format(board[6].count + board[8].count + board[9].count))
    print("Pink: {:.2f}".format(board[11].count + board[13].count + board[14].count))
    print("Orange: {:.2f}".format(board[16].count + board[18].count + board[19].count))
    print("Red: {:.2f}".format(board[21].count + board[23].count + board[24].count))
    print("Yellow: {:.2f}".format(board[26].count + board[27].count + board[29].count))
    print("Green: {:.2f}".format(board[31].count + board[32].count + board[34].count))
    print("Dark Blue: {:.2f}".format(board[37].count + board[39].count))


def run_game():
    place = 0
    board = init_board()
    chance, chest = init_decks()
    board[0].land(place, board, chance, chest)
    board[40].land(place, board, chance, chest)
    for i in range(30):
        place, board, chance, chest = take_turn(place, board, chance, chest)
    return board


def run_n_games(n):
    avg_board = init_board()
    for i in range(n):
        board = run_game()
        for ind, x in enumerate(board):
            avg = (((x.count / board[40].count) * 100) / n)
            avg_board[ind].add_avg(avg)
    print_board2(avg_board)
    print_by_street(avg_board)



run_n_games(10000)