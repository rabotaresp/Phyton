a = int(input("Enter number one - "))
#b = int(input("Enter number two - "))
# if a<b:
#     print(a)
# else:
#     print(b)
#2#####################
#c  = int(input("Enter number three - "))
# if a < b and b < c:
#     print(a)
# elif b < a and a < c:
#     print(b)
# else:
#     print(c)
#3#####################################
# if a == b and a == c:
#     print("3")
# if a != b and b == c or c == a or a == b and b != c or c == a:
#     print("2")
# if a != b and a != c and b != c:
#     print("0")
#4################################
#d = int(input("Enter number four - "))
# if (a + b)%2 == 0 and (c + d)%2 == 0 or (a + b)%2 != 0 and (c + d)%2 != 0:
#     print("Y")
# else:
#     print("N")
#5##############################
# if a%4==0 or a%100 != 0 and a % 400 == 0:
#     print("Y")
# else:
#     print("N")
#6############################
# if a == c or b == d:
#     print("Y")
# else:
#     print("N")
#7############################
# if (a - c)== 1 and (b - d) == 1 or (c - a) == 1 and (d - b) == 1 or (a - c)== 1 and (d - b) == 1 or (c - a) == 1 and (b - d) == 1 or (a - c)== 1 and (b - d) == 0 or (c - a) == 1 and (d - b) == 0 or (a - c)== 0 and (d - b) == 1 or (c - a) == 0 and (b - d) == 1:
#     print("Y")
# else:
#     print("N")
#8###############################
# if abs(a-c)==abs(b-d):
#     print("Y")
# else:
#     print("N")
#9#############################
# if abs(a-c)==abs(b-d) or a == c or b == d:
#     print("Y")
# else:
#     print("N")
#10##############################
# if c == a + 2 and d == b + 1 or d == b - 1 or c == a + 1 and d == b + 2 or d == b - 2:
#     print("Y")
# elif c == a - 2 and d == b + 1 or d == b - 1 or c == a - 1 and d == b + 2 or d == b - 2:
#     print("Y")
# else:
#     print("N")
#11#################################
# if a*b%c==0:
#     print("Y")
# else:
#     print("N")
#12##################################
# x = (a - d)
# y = (b - c)
# if y < x:
#     print(y)
# else:
#     print(x)
#13##################################
# x = a*2/b
# y = float(x*1.18)
# print(y)
#14################################
if not a == 11 and not a == 111 and a % 10 == 1:
    print(a, "рубль")
elif  10 >= a >= 5 or 112 <= a <= 120:
    print(a, "рублей")
elif a < 10 or a > 20:
        if a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
            print(a, "рубля")
if  a % 10 == 5 or a % 10 == 6  or a % 10 == 7  or a % 10 == 8 or a % 10 == 9 or a % 10 == 0:
    print(a, "рублей")