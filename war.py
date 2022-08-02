from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None, "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King", "Ace"]
            
    def __init__(self, value, suit):
        self.value = value
        self. suit = suit
    #less than(comparing cards)
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    #greater than(comparing cards)
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    #Print the card
    def __repr__(self):
        value = self.values[self.value] + " of " + self.suits[self.suit]
        return value
    
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self,):
        name1 = input("Player1:")
        name2 = input("Player2:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "Winner is {}"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {}, {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        print("Starting War")
        while len(cards) >= 2:
            m = "Press q to quit, Press any key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        
        win  = self.winner(self.p1, self.p2)
        print("Game over, {}".format(win))
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name + "wins"
        if p1.wins < p2.wins:
            return p2.name + "wins"
        return "It's a tie!"

game = Game()
game.play_game()
