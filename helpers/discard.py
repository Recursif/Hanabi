try:
    from constant import *
except:
    from helpers.constant import *

from helpers.cards_utility import *

def print_instruction_discard(know_infos): 
    """
        Print Discard Instructions

    """
    print("Choississez la carte à défausser :")
    print("")
    for i in range(5):
        print(str(i + 1) + "- " + know_infos[i])
    print("")



def get_card_to_discard(hand):
    """
        Retrieving card to discard

    """
    action_value = input("")
    print("")
    while (not((action_value) in ["1","2","3","4","5"])):
        print_board()
        print("Attention la valeur choisie doit être entre 1 et 5")
        print("")
        action_value = input("")
        print("")

    card_to_discard = hand[int(action_value) - 1]
    return (card_to_discard)


def remove_card_from_hand(hand,card):
    hand.remove(card)
    return hand


def remove_card_from_know_info(hand,know_infos,card):
    """
        Remove card from know info

    """
    index_card = hand.index(card)
    
    know_infos[index_card] = "? "
    return know_infos


def discard(deck,hands,know_infos,error_token,clue_token,turn,table):
    """
        Discard Function

        parameters
        ----------
        deck: list of cards on the deck

        hands: the list of the cards of the player (unknow for the current player)

        know_infos: list of the know infos

        error_token: the number of error tokens

        clue_token: the number of clue tokens

        turn: the number of the current player

        table: helping knowing if a play is a error or not

        return
        ------
        the new state for deck, hands, know_infos, error_token,
        and clue_token after the play
    """
    print_instruction_discard(know_infos)
    card = get_card_to_discard()

    # Retrieving card location
    card_num = int(card[0]) -1
    card_color = card[1]
    card_color = colors.index(card_color)

    # Tokens resolving
    if table[card_color][card_num]==1: 
        error_token += 1
        print("Erreur !")
    else:
        clue_token += 1
        print("+1 indice !")
    # Removing card from the table
    table[card_color][card_num] -= 1

    # Particular case for unfinishable color of cards
    if table[card_color][card_num]==0:
        for i in range(5-card_num):
            table[card_color][card_num+i]=0

    # Removing information from know_infos and hands
    know_infos = remove_card_from_know_infos(hand,know_infos,card)
    hand = remove_card_from_hand(hand,card)

    # Drawing
    deck,hand = draw_card(deck,hand)

    return deck,hands,know_infos,error_token,clue_token,table