
import random 

from helpers.constant import *
from helpers.printers import *
from helpers.cards_utility import *

from helpers.play import *
from helpers.discard import *
from helpers.give_clues import *

# --- Initialisation ---
# Initialisation of the board
board = ['0B','0Y','0R','0W','0G']

# Initialisation of the know infos
know_infos = []
for i in range(nb_players):
    know_infos.append(["? ","? ","? ","? ","? "])

# Initialisation of the discard table
table = []
for i in range (5):
    table.append([3,2,2,1,1])

# --- Genaration of the deck ---
# Generate the deck
deck = generate_cards()

# Shuffle the deck
random.shuffle(deck)


# --- Distribution of the hands of the different players ---

# hands the list of the different player's hand
hands = []

for i in range(nb_players):
    # hand a list of 5 cards distributed to the player
    hand = []

    for j in range(5):
        hand = draw_card(deck,hand)
    
    # for each player add his hand to the hands list
    hands.append(hand)


# print(hands)


# --- Functions to print and select the action available during the turn ---
def print_actions():
    """
        Print the difference choice of action available
    """
    print("Choississez une action parmi celles-ci:")
    print("")
    print("1- Jouer une carte")
    print("2- Défausser une carte")
    print("3- Donner un indice")
    print("4- Quittez")
    print("")

def get_action():
    """
        Get the action selected by the player

        return
        -------
        action: int 
            the action value selected
    """
    action = input("")
    print("")
    while (not((action) in ["1","2","3","4"])):
        print_board()
        print("attention la valeur choisie doit être entre 1 et 4")
        print("")
        action = input("")
        print("")
    
    return (action)




# --- Parameter of the game ---

# Number of the current player : [0 ; nb_players - 1]
turn = 0

# State of the game 
is_game_ended = False

# Number of error tokens used : [0 ; 3]
error_tokens = 0

# Number of clue tokens used : [0 ; 8]
clue_tokens = 0


print_start_game()


# --- Play until the game is not ended
"""
while (not(is_game_ended)):
    turn += 1
"""

# Print the infos on the current turn
print_players_hand(nb_players,turn,hands,know_infos)
print_board(board)

# Get the action selected by the current player
print_actions()
action = get_action()


# --- Start the selected action ---
if (action == "1"):
    deck,board,hands,know_infos = play(deck,board,hands,know_infos,turn)
elif (action == "2"):
    print("Defausser une carte n'est pas encore implemeté")
    #discard()
elif(action == "3"):
    print("Donner un indice n'est pas encore implemeté")
    #give_clues()
else:
    print("au revoir!!")
    end_game = True


print("partie terminée!")
