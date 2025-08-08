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
        for suit in suits:
            for rank in range(1, 14):
                card = Card(rank, suit)
                self.deck_of_cards.append(card)

    # TODO: Create a method/function that displays the entire deck of cards
    def display_deck(self):
        for card in self.deck_of_cards:
            card.print_card()
            
# TESTING: Create a deck of cards object and print them to the console



