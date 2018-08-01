
import random 

from helpers.generate_cards import *

cards = generate_cards()

print(cards)
shuffled_cards = cards[:]

random.shuffle(shuffled_cards)

print(shuffled_cards)

nb_players = 3

for index in range(nb_players):


