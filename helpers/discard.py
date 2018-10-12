try:
    from constant import *
    from cards_utility import *
    from printers import *
except:
    from helpers.constant import *
    from helpers.cards_utility import *
    from helpers.printers import *


def print_instruction_discard(know_infos, turn): 
    """
        Print Discard Instructions

    """
    print("Choississez la carte à défausser :")
    print("")
    print(know_infos[turn])
    for i in range(5):
        print(str(i + 1) + "- " + know_infos[turn][i])
    print("")



def get_card_to_discard(hand):
    """
        Retrieving card to discard

    """
    action_value = input("")
    print("")
    while (not((action_value) in ["1","2","3","4","5"])):
        print("Attention la valeur choisie doit être entre 1 et 5")
        print("")
        action_value = input("")
        print("")

    card_to_discard = hand[int(action_value) - 1]
    return (card_to_discard)


def discard(deck, hands, know_infos, error_token, clue_token, turn, table):
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
        the new state for deck, hands, know_infos, table, error_token,
        and clue_token after the play
    """
    print_instruction_discard(know_infos, turn)
    card = get_card_to_discard(hands[turn])

    index_card = hands[turn].index(card)
    
   

    # Retrieving card location
    card_num = int(card[0]) -1
    card_color = card[1]
    card_color = colors.index(card_color)

    # Tokens resolving
    if (table[card_color][card_num] == 1): 
        error_token += 1
        print("Erreur !")
    elif (clue_token + 1 <= 8):
        clue_token += 1
        print("+1 indice !")
    # Removing card from the table
    table[card_color][card_num] -= 1

    # Particular case for unfinishable color of cards will not be counted as an error
    if (table[card_color][card_num] == 0):
        for i in range(5 - card_num):
            table[card_color][card_num+i]=0

    # Removing information from know_infos and hands

    print(hands[turn])
    print(card)

    hands[turn].remove(card)
    know_infos[turn][index_card] = "??"

    print(hands[turn])
    # Drawing
    hands[turn] = draw_card(deck,hands[turn])

    print(hands[turn])
    return deck, hands, know_infos, error_token, clue_token, table

