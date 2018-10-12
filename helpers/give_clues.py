

try:
    from printers import print_players_hand, print_board
except:
    from helpers.printers import print_players_hand, print_board


def get_selected_hand(hands, turn):
    """
        Print instructions clues color
    """

    hand = ""
    print("")
    while (not(hand in [str(x) for x in range(1, len(hands))])):

        possible_hands = []
        if hand != "":
            print("Attention la main choisie doit être entre 1 et " + str(len(hands) - 1))

        print("Choississez la main que vous voulez selectionner")
        print("")
        j = 1
        for i in range(1, len(hands) + 1):
            if (turn != i - 1):
                
                print(str(j) + "- " + " ".join(hands[i - 1]))
                possible_hands.append(hands[i - 1])
                j += 1

        print("")
        hand = input("")
        print("")

    hand = possible_hands[int(hand) -1]
    return hand


def get_color_clue(possible_colors):
    """
        Get color given as a clue
    
    """
    
    color = ""
    print("")
    while (not(color in [str(x) for x in range(1, len(possible_colors) + 1)])):

        if color != "":
            print("Attention la valeur choisie doit être entre 1 et " + str(len(possible_colors)))

        print("Choississez la couleur pour votre indice")
        print("")
        for i in range(len(possible_colors)):
            print(str(i + 1) + "- " + str(possible_colors[i]))
        print("")
        color = input("")
        print("")
    
    color = possible_colors[int(color) - 1]
    return color


def get_number_clue(possible_numbers):
    """
        Get number given as a clue

    """
    
    number = ""
    print("")
    while (not(number in [str(x) for x in range(1, len(possible_numbers + 1))])):

        if number != "":
            print("Attention la valeur choisie doit être entre 1 et " + str(len(possible_numbers)))

        print("Choississez le nombre pour votre indice")
        print("")
        for i in range(len(possible_numbers)):
            print(str(i + 1) + "- " + str(possible_numbers[i]))
        print("")
        number = input("")
        print("")
    
    number = possible_numbers[int(number) - 1]
    return number


def get_clue_choice():
    """
        Get the type of clue
    """

    choice = ""
    print("")
    while (not(choice in ["1","2"])):

        if choice != "":
            print("Attention la valeur choisie doit être entre 1 et 2")
        print("")
        print("Donner un indice sur")
        print("")
        print("1- une couleur")
        print("2- un chiffre")
        print("")
        choice = input("")
        print("")
    
    return choice


def set_color_clue(know_infos, selected_hand, selected_hand_index, color_clue):
    """
        Set the color as a clue in know_infos

    """
    for i in range(5):
        if (selected_hand[i][1] == color_clue):
            list_know_infos = list(know_infos[selected_hand_index][i])
            list_know_infos[1] = selected_hand[i][1]
            know_infos[selected_hand_index][i] = ''.join(list_know_infos)

    return know_infos

def set_number_clue(know_infos, selected_hand, selected_hand_index, number_clue):
    """
        Set the number as a clue in know_infos

    """
    for i in range(5):
        if (selected_hand[i][0] == number_clue):
            list_know_infos = list(know_infos[selected_hand_index][i])
            list_know_infos[0] = selected_hand[i][0]
            know_infos[selected_hand_index][i] = ''.join(list_know_infos)

    return know_infos


def give_clues(hands, know_infos, turn):
    """
        Clue Giving Function

        parameters
        ----------
        hands: the list of the cards of the player (unknow for the current player)

        know_infos: list of the know infos

        turn: the number of the current player


        return
        ------
        the new state of know_infos and clue_token after giving a clue
    """

    selected_hand = get_selected_hand(hands, turn)

    print(" ".join(selected_hand))

    selected_hand_index = hands.index(selected_hand)

    possible_numbers = list(set([x[0] for x in selected_hand]))
    possible_colors = list(set([x[1] for x in selected_hand]))

    clue_choice = get_clue_choice()

    if (clue_choice == "1"):
        color_clue = get_color_clue(possible_colors)
        know_infos = set_color_clue(know_infos, selected_hand, selected_hand_index, color_clue)
    elif (clue_choice == "2"):
        number_clue = get_number_clue(possible_numbers)
        know_infos = set_number_clue(know_infos, selected_hand, selected_hand_index, number_clue)
    else:
        print("Are you hacking bro?")
    
    return know_infos
