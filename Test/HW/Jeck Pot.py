from random import choice
from random import shuffle
imena_igrokov = dict(name_i=[], name_krup=['Крупье'])
imena_igrokov['name_i'].append(input('Введите имя игрока: '))

kart = {'J':10, 'Q':10, 'K':10, 'A':11}
kart_sp = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4
shuffle(kart_sp)
kolod_i = [] #колода крупье
kolod_k = [] #колода игрока
def opr_kart(q):# перевод карт с картинками в число
    if q == 'J':
        return kart.get('J')
    if q == 'Q':
        return kart.get('Q')
    if q == 'K':
        return kart.get('K')
    if q == 'A':
        return kart.get('A')
    if type(q) == int:
        return q

for q in range(2): #рука игрока
    kolod_i.append(kart_sp.pop())

for j in range(2):#рука крупье
    kolod_k.append(kart_sp.pop())

def r_ruk_i():# сумма карт игрока
    res = 0
    for q in range(len(kolod_i)):
        res += opr_kart(kolod_i[q])
    return res

def r_ruk_k():# сумма карт крупье
    res = 0
    for q in range(len(kolod_k)):
        res += opr_kart(kolod_k[q])
    return res

print("Карты ",imena_igrokov['name_i'][0], kolod_i, "сумма карт: ", r_ruk_i())
print("Карты ",imena_igrokov['name_krup'][0], kolod_k, "сумма карт: ", r_ruk_k())

if 12<r_ruk_k()<15: #добор карт в руку крупье
    kolod_k.append(kart_sp.pop())
    r_ruk_k()
    if 17<r_ruk_k()<=21:
        print("Карты ",imena_igrokov['name_krup'][0], kolod_k, "сумма карт: ", r_ruk_k())

#условия победы
if r_ruk_i() < 21:
    answer = str(input('Хотите взять еще карту? y/n '))
    if answer != "n":
        kolod_i.append(kart_sp.pop())
        for q in range(len(kolod_i)):
            if kolod_i[q] == 'A' and q >= 2:
                kolod_i[q] = int(1)
        r_ruk_i()
        if r_ruk_i() < 21:
            print(kolod_i)
            answer = str(input('Хотите взять еще карту? y/n '))
            if answer != "n":
                kolod_i.append(kart_sp.pop())
                for q in range(len(kolod_i)):
                    if kolod_i[q] == 'A' and q >= 2:
                        kolod_i[q] = 1
                r_ruk_i()
    else:
        if r_ruk_i() == r_ruk_k():
            print('Ничья')
        elif r_ruk_i() > r_ruk_k():
            print('Игрок ',imena_igrokov['name_i'][0], 'победил')
            print("Карты ", imena_igrokov['name_i'][0], kolod_i, "сумма карт: ", r_ruk_i())
            print("Карты ",imena_igrokov['name_krup'][0], kolod_k, "сумма карт: ", r_ruk_k())
        elif r_ruk_k() > r_ruk_i():
            print('Победил ',imena_igrokov['name_krup'][0])
            print("Карты ",imena_igrokov['name_i'][0], kolod_i, "сумма карт: ", r_ruk_i())
            print("Карты ",imena_igrokov['name_krup'][0], kolod_k, "сумма карт: ", r_ruk_k())
if r_ruk_i() == 21:
    if r_ruk_i() == r_ruk_k():
        print('Ничья')
    elif r_ruk_i() > r_ruk_k():
        print('Игрок ',imena_igrokov['name_i'][0], 'победил')
    print("Карты ",imena_igrokov['name_i'][0], kolod_i, 'У Вас 21, ПОЗДРАВЛЯЕМ!!!')
if r_ruk_i() > 21:
    print('Победил ', imena_igrokov['name_krup'][0])
    print('У Вас', kolod_i, ' сумма', r_ruk_i(), 'ПЕРЕБОР, очень жаль ВЫ неудачник')
if kolod_i[0] == 'A' and kolod_i[1] == 'A':
    print("Карты ", imena_igrokov['name_i'][0], kolod_i, 'У Вас GOLD 21, ПОЗДРАВЛЯЕМ!!!')
if r_ruk_k() == 21:
    if r_ruk_i() == r_ruk_k():
        print('Ничья')
    # elif r_ruk_i() < r_ruk_k():
        # print('Победил ', imena_igrokov['name_krup'][0])
    print('У ',imena_igrokov['name_krup'][0], kolod_k, '21, игрок ',imena_igrokov['name_i'][0], 'проиграл')
input('Нажмите ввод чтобы выйти ...')