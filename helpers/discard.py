
try:
    from constant import *
    from cards_utility import *
except:
    from helpers.constant import *
    from helpers.cards_utility import *


# --- Discard Instructions ---

def print_instruction_discard(know_infos): 
    print("Choississez la carte à défausser :")
    print("")
    for i in range(5):
        print(str(i + 1) + "- " + know_infos[i])
    print("")


# --- Retrieving card to discard ---

def get_card_to_discard(hand):
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


# --- Discard Function ---


def discard():
    print_instruction_discard()
    card = get_card_to_discard()

    # Retrieving card location
    card_num = int(card_to_discard[0]) -1
    card_color = card_to_discard[1]
    card_color = colors.index(card_color)

    # Tokens resolving
    if table[card_color][card_num]==1: 
        error_token += 1    
    else:
        clue_token += 1
    # Removing card from the table
    table[card_color][card_num] -= 1

    # Particular case for unfinishable color of cards
    if table[card_color][card_num]==0:
        for i in range(5-card_num):
            table[card_color][card_num+i]=0