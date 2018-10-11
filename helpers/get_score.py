

try:
    from constant import *
except:
    from helpers.constant import *


def get_score(board):
    """
        Get the score from the board

        return
        -------
        action: int 
            the score
    """
    score = 0
    for card in board:
        score += int(card[0])
    return (score)

