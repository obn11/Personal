class Game():
    """Stores deck, players hands and table sets"""
    
    def __init__(self, position, hand, pile, num_players):
        self.deck = initialize_deck()
        self.hand = hand
        self.position = position
        self.others = []
        self.pile = [pile]
        self.table = []
        self.num_players = num_players
        
    def o_turn(self,t):
        """'"""
        print("player {}'s turn".format(t))
        choice = input('deck or pile? ')
        
        if choice.strip() == 'pile':
            top = self.pile.pop()
            self.deck[top] = 'P{}'.format(t)
            
        table = input('any table cards? ')
        while table not in ('no', 'No', 'n', 'N'):
            table = table.split()
            self.table.append(table)
            if len(table) > 1:
                self.table[t-1] += (table) 
            else:
                prompt = input('where? (player, numset) ')
                x, y = prompt.split(', ')
                self.table[x-1][y-1].append(table)
            for i in table:
                self.deck[i] = 'T'
            table = input('any others? ')
                
        output = input('What was their discard? ')
        self.deck[output] = 'P'
        self.pile.append(output)       
            

def initialize_deck():
    """Creates full deck with all set to underscovered
    U = Undiscovered
    H = in your hand
    Pn = in player n's hand
    P = in pile
    D = in draw deck
    T = table card"""
    deck = {'AH': 'U', '2H': 'U', '3H': 'U', '4H': 'U', '5H': 'U', '6H': 'U',
            '7H': 'U', '8H': 'U', '9H': 'U', '10H': 'U', 'JH': 'U', 'QH': 'U', 'KH': 'U',
            'AD': 'U', '2D': 'U', '3D': 'U', '4D': 'U', '5D': 'U', '6D': 'U',
            '7D': 'U', '8D': 'U', '9D': 'U', '10D': 'U', 'JD': 'U', 'QD': 'U', 'KD': 'U',
            'AS': 'U', '2S': 'U', '3S': 'U', '4S': 'U', '5S': 'U', '6S': 'U',
            '7S': 'U', '8S': 'U', '9S': 'U', '10S': 'U', 'JS': 'U', 'QS': 'U', 'KS': 'U',
            'AC': 'U', '2C': 'U', '3C': 'U', '4C': 'U', '5C': 'U', '6C': 'U',
            '7C': 'U', '8C': 'U', '9C': 'U', '10C': 'U', 'JC': 'U', 'QC': 'U', 'KC': 'U',
            'JB': 'U', 'JR': 'U'}
    return deck

def start():
    """'"""
    num_players = int(input('how many players are there? '))
    position = int(input('what is your starting position? (1 if first) '))
    hand = input('what is your starting hand? ').split()
    pile = input('what is the first card in the pile? ')
    G = Game(position, hand, pile, num_players)
    for n in range(1, num_players+1):
        G.others.append([])
        G.table.append([])
    for i in G.hand:
        G.deck[i] = 'H'
    G.deck[pile] = 'P'
    return G

def run():
    """'"""
    G = start()
    t = 1
    done = False
    while not done:
        if t == G.position:
            #G.y_turn()
            #t += 1
            print('Your turn (P{})'.format(t))
            return G
        else:
            G.o_turn(t)
            t += 1
        if t > G.num_players:
            t = 1
#3H 4H KS 6D 2S QH 8C

G = run()