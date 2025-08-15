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
            rand_index = random.randint(index + 1, len(self.deck_of_cards) - 1)
            current_card = self.deck_of_cards[index]
            # print("Index: {} Num: {}".format(index, rand_index))
            self.deck_of_cards[index] = self.deck_of_cards[rand_index]
            self.deck_of_cards[rand_index] = current_card
    
    # TODO 1.1: Create a method/function for dealing cards to players
    # BRAINSTORM: What information does this function need?
    # TODO 1.2: Allow the function to have access to the class itself and receive
        # the player object/name (2 parameters)
        # TODO 2: Inside of the function -
            # Add code that checks if there are cards in the list
            # HINT: len(list_name)
            # TODO 3: Inside of the if-else statement for when there are cards -
            # Store a random card from the deck of cards (HINT: random.choice)
            # Give the player the random card (AKA: Add it to their hand)
            # Remove the random card from the deck of cards
    def deal_cards(self, player):
        if (len(self.deck_of_cards) > 0):
            rand_card = random.choice(self.deck_of_cards)
            player.hand.append(rand_card)
            self.deck_of_cards.remove(rand_card)
        else:
            print("Empty deck!")
            
    # TODO: Create a method/function that displays the entire deck of cards
    def display_deck(self):
        for card in self.deck_of_cards:
            card.print_card()
            
# TESTING: Create a deck of cards object and print them to the console
