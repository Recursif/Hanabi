
import random 

from helpers.generate_cards import *

cards = generate_cards()

deck = cards[:]

random.shuffle(deck)

nb_players = 3

board = ['**','**','**','**','**']

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

"""
while (not(end_game)):
    print_game()
    print("Choisissez un action ")
    if (i):
        end_game = True
"""


print("partie terminée")




            



#def defausse():
