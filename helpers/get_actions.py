

def get_action_from_player():
    """
        Get the action selected by the player

        return
        -------
        action: int 
            the action value selected
    """
    action = input("")
    print("")
    while (not((action) in ["1","2","3","4"])):
        print_board()
        print("Attention la valeur choisie doit être entre 1 et 4")
        print("")
        action = input("")
        print("")
    
    return (action)
    