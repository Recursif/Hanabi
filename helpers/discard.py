table = []
error = 0
token = 0


colors = [
    "B",
    "Y",
    "R",
    "W",
    "G",
]

def get_card_to_discard(hand):
    action_value = input("")
    print("")
    while (not((action_value) in ["1","2","3","4","5"])):
        print_board()
        print("attention la valeur choisie doit être entre 1 et 5")
        print("")
        action_value = input("")
        print("")

    card_to_discard = hand[int(action_value) - 1]
    return (card_to_discard)


    """
        Draw card function

        return hand with a one more card if the deck not empty

    """

def discard():
    print_instruction_discard()
    card = get_card_to_discard()
    


#table generation
for i in range (5):
    table.append([3,2,2,1,1])

#récupération de l'emplacement de la carte
card_num = int(card[0]) -1
card_color = card[1]
card_color = colors.index(card_color)

#résolution des erreurs et tokens
if table[card_color][card_num]==1: 
    error += 1    
else:
    token += 1

#carte retirée de la liste
table[card_color][card_num] -= 1

#si pile de couleur non finissable, carte de valeur supérieure ne compte pas comme des erreurs
if table[card_color][card_num]==0:
    for i in range(5-card_num):
        table[card_color][card_num+i]=0

#print (table)