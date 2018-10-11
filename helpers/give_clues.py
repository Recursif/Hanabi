

try:
    from printers import print_players_hand, print_board
except:
    from helpers.printers import print_players_hand, print_board


def get_player_clue(nb_players,turn,hands,know_infos,board):
    """
        Retrieve Player Choosen to give a clue

    """
    action_player = ""
    print("")

    while (not((action_player) in range(nb_players-1))):
        print_players_hand(nb_players,turn,hands,know_infos)
        print_board(board)
        if action_player != "":
            print("Attention la valeur choisie doit être entre 1 et",nb_players)
        print("")
        print("À quel joueur donner un indice ?")
        print("")

        for i in range(nb_players):
            if i != turn:
                print(str(i) + "- " + " ".join(hands[i]))
            else:
                print(str(i) + "- C'est votre main !")
        
        print("")
        action_player = input("")
        print("")

        # Evitement du cas où le joueur voudarit donner un indice sur son propre jeu
        
        return action_player


def get_clue_type(nb_players,turn,hands,know_infos,board):
    """
        Retrieve clue type (numeral or color) given by the player
    
    """
    action = ""

    print("")
    while (not((action) in ["1","2"])):
        print_players_hand(nb_players,turn,hands,know_infos)
        print_board(board)

        if action != "":
            print("Attention la valeur choisie doit être entre 1 et 2")
        print("")
        print("Donner un indice sur")
        print("")
        print("1- une couleur")
        print("2- un chiffre")
        print("")
        action = input("")
        print("")
    
    return action


def get_color_clue(action_player,hands):
    """
        Retrieve color given as a clue by the player

    """    
    possible_color = []
    action_color = ""
    hand = hands[action_player]

    for i in range(5):
        possible_color.append(hand[i][1])

    possible_color = set(possible_color)
    
    while (not((action_color) in possible_color)):
        if action_color != "":
            print("Attention la valeur choisie doit être valide")
        
        for i in possible_color:
            print(possible_color)
    
        action_color = input("Quelle couleur donner comme indice ?")

    return action_color


def color_clue_giving(action_player,action_color,know_infos,hands):
    """
        Change know_infos function of color clue given

    """
    for i in range(5):
        if hands[action_player][i][1] == action_color:
            know_infos[action_player][i][1] == hands[action_player][i][1]

    return know_infos
        

def get_numeral_clue(action_player,hands):
    """
        Retrieve numeral given as a clue by the player

    """
    possible_numeral = []
    action_numeral = ""
    hand = hands[action_player]

    for i in range(5):
        possible_numeral.append(hand[i][1])

    possible_numeral = set(possible_numeral)
    
    while (not((action_numeral) in possible_numeral)):
        if action_numeral != "":
            print("Attention la valeur choisie doit être valide")
        
        for i in possible_numeral:
            print(possible_numeral)

        action_numeral = input("Quelle chiffre donner comme indice ?")

    return action_numeral


def numeral_clue_giving(action_player,action_numeral,know_infos,hands):
    """
        Change know_infos function of numeral clue given

    """
    for i in range(5):
        if hands[action_player][i][0] == action_numeral:
            know_infos[action_player][i][0] == hands[action_player][i][0]

    return know_infos




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
    
    action_player = get_player_clue(nb_players,turn,hands,know_infos,board)
    action = get_clue_type(nb_players,turn,hands,know_infos,board)

    if action == 1:
        action_color = get_color_clue(action_player,hands)
        know_infos = color_clue_giving(action_player,action_color,know_infos,hands)
    elif action == 2:
        action_numeral = get_numeral_clue(action_player,hands)
        know_infos = numeral_clue_giving(action_player,action_numeral,know_infos,hands)

