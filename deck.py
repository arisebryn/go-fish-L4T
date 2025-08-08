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
                card = Card(rank, suit)
                self.deck_of_cards.append(card)
                # Create a card object (set the rank and the suit)
                # Add the object to the empty deck_of_cards list

    def shuffle(self):
        for index in range(len(self.deck_of_cards) - 1):
            num = random.randint(index + 1, len(self.deck_of_cards) - 1)
            temp = self.deck_of_cards[index]
            # print("Index: {} Num: {}".format(index, num))
            self.deck_of_cards[index] = self.deck_of_cards[num]
            self.deck_of_cards[num] = temp

    # TODO: Create a method/function that displays the entire deck of cards
    def display_deck(self):
        for card in self.deck_of_cards:
            card.print_card()
            
# TESTING: Create a deck of cards object and print them to the console



