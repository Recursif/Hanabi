

def print_players_hand(nb_players,turn,hands_list,know_list):
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


def print_board(board):
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