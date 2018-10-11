

try:
    from constant import *
except:
    from helpers.constant import *


def init_know_infos(nb_players):
    know_infos = []
    for i in range(nb_players):
        know_infos.append(["? ","? ","? ","? ","? "])
    
    return know_infos


def init_discard_table():
    table = []
    for i in range (5):
        table.append([3,2,2,1,1])