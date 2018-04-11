from random import shuffle
from random import choice

def start_game():
    kart = ['6','7','8','9','10','J','Q','K','A']*4
    return choice(kart)
print(start_game())
def sum_kart():
    if start_game() == 'J':
        return 10
    elif start_game() == 'Q':
        return 10
    elif start_game() == 'K':
        return 10
    elif start_game() == 'A':
        return 10
    