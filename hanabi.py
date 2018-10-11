
import random 

from helpers.init import init_know_infos, init_discard_table
from helpers.cards_utility import generate_cards, draw_card, distribute_hands
from helpers.printers import print_start_game, print_players_hand, print_board

from helpers.get_actions import get_action_from_player
from helpers.play import play
from helpers.discard import discard
from helpers.give_clues import give_clues

from helpers.get_score import get_score
from helpers.check_end_game import check_end_game

# --- Initialisation ---
# Initialisation of the board
board = ['0B','0Y','0R','0W','0G']

# Number of players
nb_players = 3

# Initialisation of the know infos
know_infos = init_know_infos(nb_players)

# Initialisation of the discard table
table = init_discard_table()


# --- Genaration of the deck ---
# Generate the deck
deck = generate_cards()

# Shuffle the deck
random.shuffle(deck)


# --- Distribution of the hands of the different players ---

# hands the list of the different player's hand
hands = distribute_hands(nb_players, deck)


# --- Parameter of the game ---

# The number of player :
nb_players = 3

# Number of the current player : [0 ; nb_players - 1]
turn = 0

# State of the game 
is_game_ended = False

# Number of error tokens used : [0 ; 3]
error_token = 0

# Number of clue tokens used : [0 ; 8]
clue_token = 8

# Number of turn player after the empty deck : [0 ; nb_players]
turn_after_empty_deck = 0

print_start_game()


# --- Play until the game is not ended
while (not(is_game_ended)):
    # Print the infos on the current turn
    print_players_hand(nb_players,turn,hands,know_infos)
    print_board(board)

    # Get the action selected by the current player
    action = get_action_from_player(clue_token)

    # --- Start the selected action ---
    
    if (action == "1"):
        deck, board, hands, know_infos, error_token = play(deck,board,hands,know_infos,error_token,turn)
    elif (action == "2"):
        deck,hands, know_infos, error_token, clue_token, table = discard(deck,hands,know_infos,error_token,clue_token,turn,table)
    elif(action == "3"):
        print("Donner un indice n'est pas encore implemeté")
        #give_clues()
    else:
        print("Au revoir !!")
        is_game_ended = True
        print("")
    

    
    # Check if the game is endded
    if (not(is_game_ended)):
        is_game_ended = check_end_game(error_token, board, nb_players)
    
    
    # Check if the game is finish because of the lack of cards
    if (turn_after_empty_deck >= nb_players):
        print("")    
        print("Vous avez Perdu!!")
        print("")
        print("Score : " + get_score(board))
        print("")
        is_game_ended = True


    # Increment the turn_after_empty-deck variable if the deck is empty
    if (len(deck) <= 0):
        print("")    
        print("Il vous reste " + str(nb_players - turn_after_empty_deck) + " pour gagner!")
        print("")    
        turn_after_empty_deck += 1

    
    # Increment the turn
    if (turn + 1 >= nb_players - 1):
        turn = 0
    else:
        turn += 1

