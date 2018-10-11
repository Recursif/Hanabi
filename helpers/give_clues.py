

try:
    from printers import print_players_hand, print_board
except:
    from helpers.printers import print_players_hand, print_board


def get_player_selected(hands, nb_players, turn):
    """
        Print instructions clues color
    """

    hand = ""
    print("")
    while (not((hand) in [x for x in range(len(nb_players) - 1)])):

        if hand != "":
            print("Attention la main choisie doit être entre 1 et " + str(len(nb_players) - 1))

        print("Choississez la main que vous voulez selectionner")
        print("")
        for i in range(len(hands)):
            print(str(i) + "- " + " ".join(hands[i]))
        print("")
        hand = input("")
        print("")

    return color


def get_color_clue(possible_colors):
    """
        Get color given as a clue
    
    """
    
    color = ""
    print("")
    while (not((color) in [x for x in range(len(possible_colors))])):

        if color != "":
            print("Attention la valeur choisie doit être entre 1 et " + str(len(possible_colors)))

        print("Choississez la couleur pour votre indice")
        print("")
        for i in range(len(possible_colors)):
            print(str(i) + "- " + str(possible_colors[i]))
        print("")
        color = input("")
        print("")
    
    return color


def get_number_clue(possible_number):
    """
        Get number given as a clue

    """
    
    number = ""
    print("")
    while (not((number) in [x for x in range(len(possible_number))])):

        if number != "":
            print("Attention la valeur choisie doit être entre 1 et " + str(len(possible_number)))

        print("Choississez la couleur pour votre indice")
        print("")
        for i in range(len(possible_number)):
            print(str(i) + "- " + str(possible_number[i]))
        print("")
        number = input("")
        print("")
    
    return number


def get_clue_choice():
    """
        Get the type of clue
    """

    choice = ""
    print("")
    while (not((choice) in ["1","2"])):

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


def give_clues(turn,hands,know_infos,board,clue_token,nb_players):
    """
        Clue Giving Function

        parameters
        ----------
        hands: the list of the cards of the player (unknow for the current player)

        know_infos: list of the know infos

        board: cards already played

        clue_token: the number of clue tokens

        turn: the number of the current player

        action_color: empty if player give numeral clue

        action_numeral: empty if player give color clue


        return
        ------
        the new state of know_infos and clue_token after giving a clue
    """

    selected_player = get_player_selected(nb_players, turn)


    print_instructions_clues()

    clue_choice = get_clue_choice()

    if (clue_choice == 1):
        action_color = get_color_clue(action_player,hands)
        know_infos = color_clue_giving(action_player,action_color,know_infos,hands)
    elif (clue_choice == 2):
        action_numeral = get_numeral_clue(action_player,hands)
        know_infos = numeral_clue_giving(action_player,action_numeral,know_infos,hands)
    else:
        print("Are you hacking bro?")
    


