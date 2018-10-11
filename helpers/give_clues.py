
try:
    from constant import *
    from printers import print_players_hand, print_board
except:
    from helpers.constant import *
    from helpers.printers import print_players_hand, print_board



def get_color_clue(possible_colors):
    """
        Print instructions clues color
    """

    
    color = ""
    print("")
    while (not((color) in [x for x in range(len(possible_colors))])):

         if color != "":
                print("Attention la valeur choisie doit être entre 1 et " + len(possible_colors))

        print("Choississez la couleur pour votre indice")
        print("")
        for i in range(len(possible_colors)):
            print(str(i) + "- " + str(possible_colors[i]))
        print("")
        color = input("")
        print("")
    
    return color

def get_number_clue(possible_number):
    """
        Print instructions clues number
    """

    
    number = ""
    print("")
    while (not((number) in [x for x in range(len(possible_number))])):

         if color != "":
                print("Attention la valeur choisie doit être entre 1 et " + len(possible_number))

        print("Choississez la couleur pour votre indice")
        print("")
        for i in range(len(possible_number)):
            print(str(i) + "- " + str(possible_number[i]))
        print("")
        number = input("")
        print("")
    
    return number


def get_color_clue(possible_colors):
    """
        Print instructions clues color
    """

    
    color = ""
    print("")
    while (not((color) in [x for x in range(len(possible_colors))])):

         if color != "":
                print("Attention la valeur choisie doit être entre 1 et " + len(possible_colors))

        print("Choississez la couleur pour votre indice")
        print("")
        for i in range(len(possible_colors)):
            print(str(i) + "- " + str(possible_colors[i]))
        print("")
        color = input("")
        print("")
    
    return color




def get_clue_choice():
    """
        Retrieve Clue Giving Choice

    """

    action = ""
    print("")
    while (not((action) in ["1","2"])):
        print_board()

        if action != "":
            print("Attention la valeur choisie doit être entre 1 et 2")
        print("")
        print("Donner un indice sur")
        print("")
        print("1- une couleur")
        print("2- un chiffre")
        print("")
        action = input("")
        print("")

    return action_value


def give_clues(turn, hands, know_infos, board, clue_token):
    """
        Clue Giving Function

        parameters
        ----------
        hands: the list of the cards of the player (unknow for the current player)

        know_infos: list of the know infos

        board: 

        clue_token: the number of clue tokens

        turn: the number of the current player


        return
        ------
        the new state of know_infos and clue_token after giving a clue
    """

    selected_player = get_player_selected(nb_players, turn)


    print_instructions_clues()

    clue_choice = get_clue_choice()

    if (clue_choice == 1):
        print_instructions_clues_color()
    elif (clue_choice == 2):
        print_instructions_clues_digit()
    else:
        print("Are you hacking bro?")
    


