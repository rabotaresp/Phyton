from random import shuffle


def welcome_game():
    print("Welcome to 21 Game")
    name = input('Please, enter your name: ')
    return name


def tuz(summ):
    if summ >= 11:
        return 1
    else:
        return 11


def kart_conv(karta):
    if karta == 'J':
        return 2
    elif karta == 'Q':
        return 3
    elif karta == 'K':
        return 4
    elif karta is 'A':
        return 11
    else:
        return karta


def summ_count(storage):
    res = 0
    for q in storage:
        res += kart_conv(q)
    return res


def main_koloda():
    koloda = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
    shuffle(koloda)
    return koloda


def koloda_pop(koloda):
    return koloda.pop()


def player_game(name, hand, koloda):
    while True:
        if summ_count(hand) == 22 and len(hand) == 2:
            # print(name,hand,summ_count(hand))
            print(name, 'You have Gold 21')
            break
        elif summ_count(hand) > 21:
            # print(name, hand, summ_count(hand))
            print(name, 'You buster!')
            break
        answer = input(name + ', Play again?, y/n\n')
        if answer == 'y':
            hand.append(koloda_pop(koloda))
            print(name, hand, summ_count(hand))
            continue
        else:
            break
    return hand


def winner(dict, name1, name2):
    if summ_count(dict[name1]) > summ_count(dict[name2]):
        if summ_count(dict[name1]) <= 21:
            print(name1, 'is WINNER!!!')
        else:
            print(name2, 'is WINNER!!!')
    elif summ_count(dict[name2]) > summ_count(dict[name1]):
        if summ_count(dict[name2]) <= 21:
            print(name2, 'is WINNER!!!')
        else:
            print(name1, 'is WINNER!!!')
    elif summ_count(dict[name1]) == summ_count(dict[name2]):
        print("DRAW! No WINNERS!")
    else:
        print('All LOOSE!!!')


# main
def game():
    name = welcome_game()
    koloda = main_koloda()
    storage = {
        '{}'.format(name): [],
        'Dealer': []
    }
    players = [name, 'Dealer']
    for name in players:
        for q in range(2):
            storage['{}'.format(name)].append(koloda_pop(koloda))

    for q in storage:
        print(q, storage[q], 'Your Sum is ->', summ_count(storage[q]))

    for q in players:
        player_game(q, storage[q], koloda)

    winner(storage, players[0], players[1])


if __name__ == '__main__':
    game()


input('Press enter for exit...')