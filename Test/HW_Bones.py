import random
print('Для выхода из игры введите любой символ не соответствующий цифре')
answer = str()
while answer != "n":
    x = input("Выбирете тип игры: \n Игра угадай чисело (с PC), введите 1: \n Игра угадай число (Один игрок), введите 2: "
              " \n Игра угадай число (Два игрока), введите 3: \n Игра угадай число, за ограниченное количество ходов, \nвведите 4: "
              "\n Игра угадай чисело (с PC) с учетом очков, введите 5: \n Игра угадай число (Один игрок) с учетом очков, введите 6: "
              " \n Игра угадай число (Два игрока) с учетом очков, введите 7: \n Игра угадай число, за ограниченное количество ходов с учетом очков,"
              " \nвведите 8: \n -")
    a = x
    y = x
    if a.isdigit() == True:
        if int(a) == 1:# игра угадай число с компьютером, простая
            print("Игра угадай число. Числа будут меняться рандомно,\n "
                  "Вы и компьютер, по очереди, будете вводить значение.\n "
                  "Выйграет тот, кто угадает первым.""\nВводите число пока не угадаете ;)")
            while answer != "n":
                while a.isdigit():
                    b1 = random.randint(1, 6)
                    b2 = random.randint(1, 6)
                    bones = b1 + b2
                    y1 = random.randint(1, 6)
                    y2 = random.randint(1, 6)
                    bonesNPC = y1 + y2
                    x = input("Введите свое число: ")
                    a = x
                    if a.isdigit() == True:
                        if int(x) == bones:
                            print("Ваше число ", x)
                            print("Число компьютера ", bonesNPC)
                            print("Загаданое число ", bones)
                            print("ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!!!")
                            break
                        elif bonesNPC == bones:
                            print("Ваше число ", x)
                            print("Число компьютера ", bonesNPC)
                            print("Загаданое число ", bones)
                            print("Компьютер выйграл, нам жаль!!!")
                            break
                        else:
                            print("Ваше число ", x)
                            print("Число компьютера ", bonesNPC)
                            print("Загаданое число ", bones)
                            print("Вы не угадали. Попробуйте снова")
                            continue
                answer = str(input("Продолжить? y/n "))
            answer = str(input("Вернуться в игру? y/n "))
        elif int(a) == 2:# игра угадай число, простая
            print("Игра угадай число. Числа будут меняться рандомно,""\nВводите число пока не угадаете ;)")
            while answer != "n":
                while a.isdigit():
                    b1 = random.randint(1, 6)
                    b2 = random.randint(1, 6)
                    bones = b1 + b2
                    x = input("Введите свое число: ")
                    a = x
                    if a.isdigit() == True:
                        if int(x) == bones:
                            print("Ваше число ", x)
                            print("Загаданое число ", bones)
                            print("ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!!!")
                            break
                        else:
                            print("Ваше число ", x)
                            print("Загаданое число ", bones)
                            print("Вы не угадали. Попробуйте снова")
                            continue
                answer = str(input("Продолжить? y/n "))
            answer = str(input("Вернуться в игру? y/n "))
        elif int(a) == 3:# игра угадай число два игрока, простая
            print("Игра угадай число. Числа будут меняться рандомно,\n "
                  "Вы и второй игрок, по очереди, будете вводить значение.\n "
                  "Выйграет тот, кто угадает первым.""\nВводите число пока не угадаете ;)")
            name1 = input("Введите имя 1 игрока: ")
            name2 = input("Введите имя 2 игрока: ")
            while answer != "n":
                while a.isdigit() and y.isdigit():
                    b1 = random.randint(1, 6)
                    b2 = random.randint(1, 6)
                    bones = b1 + b2
                    print(name1)
                    x = input("Введите свое число: ")
                    print(name2)
                    y = input("Введите свое число: ")
                    a = x

                    if a.isdigit() == True and y.isdigit() == True:
                        if int(y) == int(x) and int(x) == bones:
                            print("Число ", name1, x)
                            print("Число ", name2, y)
                            print("Загаданое число ", bones)
                            print("Ничья, попробуйте снова")
                            break
                        elif int(y) == bones:
                            print("Число ", name1, x)
                            print("Число ", name2,y)
                            print("Загаданое число ", bones)
                            print(name2, "выйграл(а), поздравляем!!!")
                            break
                        elif int(x) == bones:
                            print("Число ", name1, x)
                            print("Число ", name2, y)
                            print("Загаданое число ", bones)
                            print(name1, "выйграл(а), поздравляем!!!")
                            break
                        else:
                            print("Число ", name1, x)
                            print("Число ", name2, y)
                            print("Загаданое число ", bones)
                            print("Вы оба не угадали. Попробуйте снова")
                            continue
                answer = str(input("Для выхода нажмите: 'n' "))
            answer = str(input("Вернуться в игру? y/n "))
        elif int(a) == 4:#Угадай число за количество попыток
            print("Игра угадай число за определенное количество попыток.\n Укажите число попыток, за которое сможете угадать число.\n Затем вводите значение чисел"
                  " пока не угадаете. \n Выпадение чисел рандомное. Удачи ;)")
            chans = int(input("Введите количество попыток: "))
            for q in range(chans):
                b1 = random.randint(1, 6)
                b2 = random.randint(1, 6)
                bones = b1 + b2
                x = input("Введите свое число: ")
                q = q + 1
                if int(q) < chans:
                    if int(x) == bones:
                        print("Ваше число ", x)
                        print("Загаданое число ", bones)
                        print("ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!!!")
                        break
                    else:
                        print("Ваше число ", x)
                        print("Загаданое число ", bones)
                        continue
                elif int(q) == chans:
                    print("Загаданое число ", bones)
                    print("Попытки закончились, Вы проиграли. Очень жаль (")
                    answer = str(input("Вернуться к выбору игры? y/n "))
        elif int(a) == 5:# игра угадай число с компьютером, сложная
            print("Игра угадай число. Числа будут меняться рандомно,\n "
                  "Вы и компьютер, по очереди, будете вводить значение.\n "
                  "Выйграет тот, кто угадает первым.""\nВводите число пока не угадаете ;)")
            while answer != "n":
                bank = int(input("Укажите размер банка: "))
                con = int(input("Укажите размер ставки: "))
                bankUs = bank
                bankPC = bank
                while a.isdigit() and bankUs !=0 and bankPC != 0 :
                    b1 = random.randint(1, 6)
                    b2 = random.randint(1, 6)
                    bones = b1 + b2
                    y1 = random.randint(1, 6)
                    y2 = random.randint(1, 6)
                    bonesNPC = y1 + y2
                    x = input("Введите свое число: ")
                    a = x
                    if a.isdigit() == True and bankUs !=0 and bankPC != 0:
                        if int(x) == bones:
                            print("Ваше число ", x)
                            print("Число компьютера ", bonesNPC)
                            print("Загаданое число ", bones)
                            print("ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!!!")
                            bankUs = bankUs + con
                            bankPC = bankPC - con
                            print("Ваши очки: ", bankUs)
                            print("Очки PC: ", bankPC)
                            continue
                        elif bonesNPC == bones:
                            print("Ваше число ", x)
                            print("Число компьютера ", bonesNPC)
                            print("Загаданое число ", bones)
                            print("Компьютер выйграл, нам жаль!!!")
                            bankUs = bankUs - con
                            bankPC = bankPC + con
                            print("Ваши очки: ", bankUs)
                            print("Очки PC: ", bankPC)
                            continue
                        else:
                            print("Ваше число ", x)
                            print("Число компьютера ", bonesNPC)
                            print("Загаданое число ", bones)
                            print("Вы не угадали. Попробуйте снова")
                            bankUs = bankUs - con
                            bankPC = bankPC - con
                            print("Ваши очки: ", bankUs)
                            print("Очки PC: ", bankPC)
                            continue
                answer = str(input("Продолжить? y/n "))
            answer = str(input("Вернуться в игру? y/n "))
        elif int(a) == 6:# игра угадай число, сложная
            print("Игра угадай число. Числа будут меняться рандомно,""\nВводите число пока не угадаете ;)")
            while answer != "n":
                bank = int(input("Укажите размер банка: "))
                con = int(input("Укажите размер ставки: "))
                bankUs = bank
                while a.isdigit() and bankUs !=0:
                    b1 = random.randint(1, 6)
                    b2 = random.randint(1, 6)
                    bones = b1 + b2
                    x = input("Введите свое число: ")
                    a = x
                    if a.isdigit() == True and bankUs !=0:
                        if int(x) == bones:
                            print("Ваше число ", x)
                            print("Загаданое число ", bones)
                            print("ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!!!")
                            bankUs = bankUs + con
                            print("Ваши очки: ", bankUs)
                            continue
                        else:
                            print("Ваше число ", x)
                            print("Загаданое число ", bones)
                            print("Вы не угадали. Попробуйте снова")
                            bankUs = bankUs - con
                            print("Ваши очки: ", bankUs)
                            continue
                answer = str(input("Продолжить? y/n "))
            answer = str(input("Вернуться в игру? y/n "))
        elif int(a) == 7:# игра угадай число два игрока, сложная
            print("Игра угадай число. Числа будут меняться рандомно,\n "
                  "Вы и второй игрок, по очереди, будете вводить значение.\n "
                  "Выигрывает тот, кто угадает первым.""\nВводите число пока не угадаете ;)")
            name1 = input("Введите имя 1 игрока: ")
            name2 = input("Введите имя 2 игрока: ")
            while answer != "n":
                bank = int(input("Укажите размер банка: "))
                con = int(input("Укажите размер ставки: "))
                bankUs1 = bank
                bankUs2 = bank
                while a.isdigit() and y.isdigit() and bankUs1 !=0 and bankUs2 != 0:
                    b1 = random.randint(1, 6)
                    b2 = random.randint(1, 6)
                    bones = b1 + b2
                    print(name1)
                    x = input("Введите свое число: ")
                    print(name2)
                    y = input("Введите свое число: ")
                    a = x
                    if a.isdigit() == True and y.isdigit() == True and bankUs1 !=0 and bankUs2 != 0:
                        if int(y) == int(x) and int(x) == bones:
                            print("Число ", name1, x)
                            print("Число ", name2, y)
                            print("Загаданое число ", bones)
                            print("Ничья, попробуйте снова")
                            bankUs1 = bankUs1
                            bankUs2 = bankUs2
                            print(name1, "Ваши очки: ", bankUs1)
                            print(name2, "Ваши очки: ", bankUs2)
                            continue
                        elif int(y) == bones:
                            print("Число ", name1, x)
                            print("Число ", name2,y)
                            print("Загаданое число ", bones)
                            print(name2, "выйграл(а), поздравляем!!!")
                            bankUs1 = bankUs1 - con
                            bankUs2 = bankUs2 + con
                            print(name1, "Ваши очки: ", bankUs1)
                            print(name2, "Ваши очки: ", bankUs2)
                            continue
                        elif int(x) == bones:
                            print("Число ", name1, x)
                            print("Число ", name2, y)
                            print("Загаданое число ", bones)
                            print(name1, "выйграл(а), поздравляем!!!")
                            bankUs1 = bankUs1 + con
                            bankUs2 = bankUs2 - con
                            print(name1, "Ваши очки: ", bankUs1)
                            print(name2, "Ваши очки: ", bankUs2)
                            continue
                        else:
                            print("Число ", name1, x)
                            print("Число ", name2, y)
                            print("Загаданое число ", bones)
                            print("Вы оба не угадали. Попробуйте снова")
                            bankUs1 = bankUs1 - con
                            bankUs2 = bankUs2 - con
                            print(name1, "Ваши очки: ", bankUs1)
                            print(name2, "Ваши очки: ", bankUs2)
                            continue
                answer = str(input("Для выхода нажмите: 'n' "))
            answer = str(input("Вернуться в игру? y/n "))
        elif int(a) == 8:#Угадай число за количество попыток, сложная
            print("Игра угадай число за определенное количество попыток.\n Укажите число попыток, за которое сможете угадать число.\n Затем вводите значение чисел"
                  " пока не угадаете. \n Выпадение чисел рандомное. Удачи ;)")
            while answer != "n":
                chans = int(input("С какой попытки угадаете? "))
                bank = int(input("Укажите размер банка: "))
                #con = int(input("Укажите размер ставки: "))
                for q in range(0, chans):
                    b1 = random.randint(1, 6)
                    b2 = random.randint(1, 6)
                    bones = b1 + b2
                    x = input("Введите свое число: ")
                    if int(x) == bones and int(q+1) == chans:
                        print("Ваше число ", x)
                        print("Загаданое число ", bones)
                        print("ВЫ СОРВАЛИ JACKPOT, ПОЗДРАВЛЯЕМ!!!")
                        bankUs = bank**10
                        print("Ваш выйгрыш", bankUs)
                        continue
                    if int(x) != bones:
                        print("Ваше число ", x)
                        print("Загаданое число ", bones)
                        print("Вы не угадали. Очень жаль (")
                        print("Осталось", chans-(q+1), "попыток")
                        continue
                    if int(x) == bones:
                        print("Ваше число ", x)
                        print("Загаданое число ", bones)
                        print("Вы  угадали. Но попытка не та ))")
                        print("Осталось", chans-(q+1), "попыток")
                        continue
                answer = str(input("Начать игру снова? y/n "))
    else:
        print("Вы ввели не корректное значение ")