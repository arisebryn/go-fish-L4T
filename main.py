# TODO CHALLENGE 1: Create a new main/game python file and then create a go fish/game class
# The constructor of the class should include
    # a deck of cards object
    # a list to store players
    # a property that tracks if the game is still being played
# HINT: Don’t forget to import any necessary files/classes at the top!
from deck import Deck

class GoFish():
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.is_playing = True
    
    def set_up(self, num_of_players):
        self.deal_pile = Deck()
        self.deal_pile.shuffle()

        




    
    # TODO CHALLENGE 2: Inside of the class, create a game setup method
    # The method should allow you to customize the number of players!
    # Inside of the method:
        # 0- Create a deck of cards object for dealing
    































# TODO CHALLENGE 2: Inside of the class, create a game setup method
# The method should allow you to customize the number of players!

# Inside of the method:
# 0- Create a deck of cards object for dealing
# 1- We want to create the number of players as player objects and add them to the list of players
# HINT: What do we create to do more than one thing at a time?
# HINT: Don't forget that each player will need an assigned name! 

# 2- We also want to track each player in the list
# HINT: What do we create for tracking information? How do we access items in a list?

# 3- If there are less than 5 players selected, deal each player 7 cards from the deck
# 4- Otherwise, deal each player 5 cards from the deck
# HINT: How do we deal cards from the deck? How would we say which player


# TODO TESTING: Outside of the class, create a function with the following
# Create a gofish/game object
# Setup the game using the new method
# Print out the list of players
# BONUS: Print out each player's hand to check their cards!


