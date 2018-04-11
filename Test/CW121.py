from random import shuffle
from random import choice

def new_game():
    koloda = {"6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10} * 4
    shuffle(koloda)
    igrok = input("Введите ваш ник:")
    diler = ()
    x=(choice(koloda))
    y=(choice(koloda))

    print("Ваша первая карта:", x, "Ваша вторая карта:", y)
    summa = x + y
    print("У вас",x+y)
    if x == 'J' or 'K' or 'Q' and y == 'J' or 'K' or 'Q':
        'A' == 1
        print('A')
    else:
        'A' == 11
        print('A')

    while summa < 21:

        ans = str(input("Хотите взять ещё одну карту? da/net "))
        if ans == 'da':
            d = (choice(koloda))
            print("Вам выпала ",d)
            summa +=d
            print("У вас",summa)
            if summa > 21:
                return("Вы проиграли")

        elif ans == 'net':
            y1 = (choice(koloda))
            x1 = (choice(koloda))
            summa_k = y1 + x1
            print("У диллера",summa_k)
            if summa_k > summa:
                return("Диллер победил")

            else:
                return("Вы победили")

print(new_game())