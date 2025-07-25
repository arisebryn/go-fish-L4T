# @TODO - Create a card class
# Set up the constructor with properties
    # HINT: Consider the important properties of a card
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    # Create a method/function that "displays" the card
    # EXAMPLE: 10 of Hearts, 1 of Spades i.e. Rank of Suit
    def print_card(self):
        print(f'{self.rank} of {self.suit}')

# TESTING: Create a card object and display the card object using the method