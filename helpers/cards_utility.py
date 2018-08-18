

try:
    from constant import *
except:
    from helpers.constant import *


def generate_cards():
    """
        Generate the card of the game

    """
    cards = []
    for color in card_color:
        #print(color)
        for index in range(len(repartition)):
            rep = repartition[index]
            #print(rep)
            for i in range(rep):
                card = str(index + 1) + color
                #print(card)
                cards.append(card)

    return(cards)


def draw_card(deck,hand):
    """
        Draw card function

        return hand with a one more card if the deck not empty

    """
    if (len(deck) >= 1):
        hand.append(deck.pop())
    else:
        print("the deck is empty")
    return hand
    






