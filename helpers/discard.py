table = []
error = 0
token = 0

card = "4R"

colors = [
    "B",
    "Y",
    "R",
    "W",
    "G",
]

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