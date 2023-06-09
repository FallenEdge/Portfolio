# Project Name: Blackjack
# Written and Programmed By: Celine Tannous
# Start Date: 09May23
# Finish Date: TBD

# program imports 
import random # for card shuffling 
import sys

# object oriented classes
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, 1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
    
class Player:
    def __init__(self):
        self.name = "Player 1"
        self.hand = []
        self.bank = 500
        self.total = 0
        self.bet = 0

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()

    def increaseBet(self, betAmount):
        self.bet += betAmount

    def showTotal(self):
        for card in self.hand:
            if card.value > 10:
                self.total += 10
            else:
                self.total += card.value
        
        return self.total

class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.total = 0

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()

    def showTotal(self):
        for card in self.hand:
            if card.value > 10:
                self.total += 10
            else:
                self.total += card.value
        
        return self.total

# main function
def main():

    print("\n--------------")
    print("Casino Vegas")
    print("--------------\n")

    print("Welcome to Casino Vegas! Here we offer a wide range of games, but unfortunately all our machines are inoperable at the moment... However, our blackjack table is available!")
    print("Please see the options below to begin your game: \n")
    
    # opening menu to begin game or close program
    print("1. Begin Game")
    print("2. Quit\n")
    menuSelect = input("Enter your selection here: ")

    errorHandling(menuSelect)

    # first option tree for the player (not correctly written, look up switch cases for syntax)
    match menuSelect:
        case "1":
            blackjack()
        case "2":
            return "Thank you for playing!\n"
        case "3":
            return 

    return 

# Error Handling Function (not fully completed, still in progress)
def errorHandling(menuSelection):
    try:
        menuSelection = int(menuSelection)

    except:
        return "This is not a valid option input. Please Try Again."
    
    if menuSelection not in ["1", "2"]:
        return "This is not one of the available options. Please try again."
    
    return

# Blackjack function
def blackjack():

    playerBust = False
    dealerBust = False

    # build deck and initialize player and dealer objects
    deck1 = Deck()
    deck1.build()
    deck1.shuffle()

    player1 = Player()
    dealer = Dealer()

    # first round draws for both the player and the dealer
    print("\nPlayer 1 Cards:")
    player1.draw(deck1)
    player1.draw(deck1)
    player1.showHand()
    print("\nCard Total: " + str(player1.showTotal()) + "\n")

    print("Dealer's Cards:")
    dealer.draw(deck1)
    dealer.draw(deck1)
    dealer.showHand()
    print("\nCard Total: " + str(dealer.showTotal()) + "\n")

    # display menu options for player

    quit()
    return
=======

    
# function calls main when program is run
if __name__ == "__main__":
    print(main())

