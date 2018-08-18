
import random 

from helpers.generate_cards import *
from helpers.printers import *

card_colors = [
    "B",
    "Y",
    "R",
    "W",
    "G",
]

def draw_card(deck,hand):
    hand.append(deck.pop())
    return hand


cards = generate_cards()

deck = cards[:]

random.shuffle(deck)

nb_players = 3

board = ['0B','0Y','0R','0W','0G']

know_cards = [
    ["? ","? ","? ","? ","? "],
    ["? ","? ","? ","? ","? "],
    ["? ","? ","? ","? ","? "]
]

#distribution des mains
hands = []

for index in range(nb_players):
    hand = []
    for i in range(5):
        hand = draw_card(deck,hand)
    hands.append(hand)


print(hands)



def get_card_to_play(hand):
    action_value = input("")
    print("")
    while (not((action_value) in ["1","2","3","4","5"])):
        print_board()
        print("attention la valeur choisie doit être entre 1 et 5")
        print("")
        action_value = input("")
        print("")

    card_to_play = hand[int(action_value) - 1]
    return (card_to_play)
        

def get_action():
    action_value = input("")
    print("")
    while (not((action_value) in ["1","2","3","4"])):
        print_board()
        print("attention la valeur choisie doit être entre 1 et 4")
        print("")
        action_value = input("")
        print("")
    
    return (action_value)

def is_valid_card_to_play(board,card):

    index_card = card_colors.index(card[1])

    number_on_board = int(board[index_card][0])

    if (number_on_board + 1 == int(card[0])):
        return (True)
    else:
        return (False)

def play_card(board,card):
    index_card = card_colors.index(card[1])

    board[index_card] = card

    return board    

def remove_card_from_end(hand,card):
    hand.remove(card)
    return hand


"""
def pop_played_card(hand,card):
    hand.pop(card)
    return hand
"""


# numéro du joueur actuel: [0 : nombre de joueurs - 1]
turn = 0

# état de la partie booléan
end_game = False

# errors_number c'est le nombre d'erreur éffectuer par les joueurs: [0 : 3]
errors_number = 0

print("\n*************\n")
print("La partie commence!!")
print("\n*************\n")

print_players_hand(nb_players,turn,hands,know_cards)
print_board(board)
print_actions()

action = get_action()

if (action == "1"):
    hand = hands[turn]
    print_instruction_play(hand)
    card = get_card_to_play(hand)

    if (is_valid_card_to_play(board,card)):
        board = play_card(board,card)
        hand = remove_card_from_end(hand,card)
        print(hand)
        hand = draw_card(deck,hand)
        print(hand)
        print(board)
    else:
        print("AhAh! Erreur! Vous perdez un point et retournez en case radis")
        errors_number += 1
elif (action == "2"):
    print("Nope")
elif(action == "3"):
    print("Nope")
else:
    print("au revoir!!")
    end_game = True


#print(action)

"""
while (not(end_game)):
    print_game()
    print("Choisissez un action ")
    if (i):
        end_game = True
"""


print("partie terminée")

#def defausse():
