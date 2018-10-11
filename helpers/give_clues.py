
try:
    from constant import *
    from printers import print_players_hand, print_board
except:
    from helpers.constant import *
    from helpers.printers import print_players_hand, print_board


def print_instructions_clues():
    """
        Print Clue Giving Instructions
    
    """

    print("Donner un indice sur")
    print("")
    print("1- une couleur")
    print("2- un chiffre")


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

    



    

def give_clues(turn,hands,know_infos,board,clue_token):
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

    #print_instructions_clues
    #print_players_hand
    #print_board

