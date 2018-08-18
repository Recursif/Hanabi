

colors = [
    "B",
    "Y",
    "R",
    "W",
    "G",
]

repartition = [3,2,2,2,1]

def generate_cards():
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




# --- Exemple pour toto --- 


# 4G 4 le nombre et G la couleur 
# cards = ["1G","1G","1G"....]

# range(5) = [0,1,2,3,4]

# print(repartition[5])

# print(len(repartition))


