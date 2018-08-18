
import random 

from helpers.generate_cards import *

card_colors = [
    "B",
    "Y",
    "R",
    "W",
    "G",
]


cards = generate_cards()

deck = cards[:]

random.shuffle(deck)

nb_players = 3

board = ['0B','0Y','0R','0W','0G']

know_list = [
    ["? ","? ","? ","? ","? "],
    ["? ","? ","? ","? ","? "],
    ["? ","? ","? ","? ","? "]
]

#distribution des mains
hands_list = []

for index in range(nb_players):
    hand_player = []
    for i in range(5):
        hand_player.append(deck.pop())
        #hand_player.append()
    hands_list.append(hand_player)
    #print(hand_player)

print(hands_list)


def print_players_hand():
    first_line = " "
    second_line = " "
    third_line = " "

    for i in range(nb_players):
        first_line += "Joueur n° " + str(i) + " " * 6
        second_line += " ".join(know_list[i])  + " " * 3
        if i != turn:
            third_line += " ".join(hands_list[i])  + " " * 3
        else:
            third_line += "X  " * 5 + " " * 2
        #second_line += 

    print(first_line)
    print("")
    print(second_line)
    print("")
    print(third_line)
    print("")

def print_board():
    first_line = "Board"
    second_line = " ".join(board)

    print(first_line)
    print("")
    print(second_line)
    print("")

def print_actions():
    print("Choississez une action parmi celles-ci:")
    print("")
    print("1- Jouer une carte")
    print("2- Défausser une carte")
    print("3- Donner un indice")
    print("4- Quittez")
    print("")

def print_instruction_play(hand):
    print("Choississez la carte que vous voulez jouer")
    print("")
    for i in range(5):
        print(str(i + 1) + "- " + hand[i])
    print("")



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



# numéro du joueur actuel: [0 : nombre de joueurs - 1]
turn = 0

# état de la partie booléan
end_game = False

# errors_number c'est le nombre d'erreur éffectuer par les joueurs: [0 : 3]
errors_number = 0

print("\n*************\n")
print("La partie commence!!")
print("\n*************\n")

print_players_hand()
print_board()
print_actions()

action = get_action()

if (action == "1"):
    print_instruction_play(hands_list[turn])
    card_to_play = get_card_to_play(hands_list[turn])

    if (is_valid_card_to_play(board,card_to_play)):
        board = play_card(board,card_to_play)
        print(board)
    else:
        print("AhAh!Erreur! Vous perdez un point et retournez en case radis")
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
