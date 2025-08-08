# TODO: Create a player file that has a class. 
# The class should allow name customization/set up, 
# should create an empty hand property, 
# and should have a score property. 
# Also, create a method/function that displays the hand

class Player:
    # Defining the constructor
    def __init__(self, name):
        self.name = name # setting up the object with the info received
        self.hand = [] # set up the hand as a new property (not custom)
        self.score = 0
    
    def display_hand(self):
        # for item_name in list_name:
        for card in self.hand:
            card.print_card()

# TESTING ONLY
p1 = Player("Miss Ari")
print(p1.name)
print(p1.hand)