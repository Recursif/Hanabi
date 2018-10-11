
try:
    from constant import *
    from printers import print_board
except:
    from helpers.constant import *
    from helpers.printers import print_board


def generate_cards():
    """
        Generate the card of the game

    """
    cards = []
    for color in colors:
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


def distribute_hands(nb_players, deck):
    """
        Distribute the hands for the player

        return
        -------
        hands: N-array size nb_players x 5 
            the different hand of the players
    """
    hands = []
    for i in range(nb_players):
        # hand a list of 5 cards distributed to the player
        hand = []

        for j in range(5):
            hand = draw_card(deck,hand)
        
        # for each player add his hand to the hands list
        hands.append(hand)

    return hands

