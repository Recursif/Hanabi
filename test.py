

possible_numeral = []
possible_color = []
liste = ["1R","2B","3G","2G","5W"]

for i in range(5):
    possible_numeral.append(liste[i][0])
    possible_color.append(liste[i][1])


possible_color = set(possible_color)
possible_numeral = set(possible_numeral)

print(possible_numeral)
print(possible_color)