# imported the class from the code file it is in
from card import Card
import random

# TODO: Create a suits list that stores all 4 as strings
suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']

# TODO: Create a class for the deck of cards
# Create constructor with no new properties
# Inside of the constructor:
    # Create an empty list
class Deck():
    def __init__(self):
        self.deck_of_cards = []
        # TODO: Create a for-each that loops through the suits
        # EX: for item_name in list_name:
            # Inside of the suits loop:
                # Create a for loop that runs 13 times (start at 1)
                    # Inside the for loop:
                    # Create a card object (set the rank and the suit)
        for suit in suits:
            for rank in range(1, 14):
                card = Card()

                # Create a card object (set the rank and the suit)
                # Add the object to the empty deck_of_cards list

    # TODO: Create a method/function that displays the entire deck of cards
    



