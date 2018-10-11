

try:
    from constant import *
    from get_score import get_score
except:
    from helpers.constant import *
    from helpers.get_score import get_score


def check_end_game(error_token, board, nb_players):

    if (error_token >= 3):
        print("")
        print("Vous avez épuisé tout vos jetons erreur!!")
        print("")
        print("Perdu!!")
        print("")
        return True
    elif (board == ['5B','5Y','5R','5W','5G'])
        print("")
        print("Félicitations, c'est gagné!!")
        print("")
        print("Score : " + get_score(board))
        print("")
        return True
    else
        return False

