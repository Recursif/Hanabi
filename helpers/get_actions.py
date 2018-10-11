

try:
    from constant import *
except:
    from helpers.constant import *


def get_action_from_player(clue_token):
    """
        Get the action selected by the player

        return
        -------
        action: int 
            the action value selected
    """
    action = ""
    print("")
    if clue_token >= 1:
        while (not((action) in ["1","2","3","Q"])):
            
            if action != "":
                print("Attention la valeur choisie doit être entre 1 et 3 ou Q")
            print("")
            print("Choississez une action parmi celles-ci:")
            print("")
            print("1- Jouer une carte")
            print("2- Défausser une carte")
            print("3- Donner un indice")
            print("Q- Quitter")           
            print("")
            action = input("")
            print("")
    else:
        while (not((action) in ["1","2","Q"])):

            if action != "":
                print("Attention la valeur choisie doit être entre 1 et 2 ou Q")
            print("")
            print("Choississez une action parmi celles-ci:")
            print("")
            print("1- Jouer une carte")
            print("2- Défausser une carte")
            print("Q- Quitter")
            print("")
            action = input("")
            print("")

    return (action)

