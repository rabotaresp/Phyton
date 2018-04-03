l = [[ 1, 2, [3, 4, 5]],['abc','qwe'], 6, 7,[8, 9]]
# def sp(l):
#     temp = []
#     for q in range (len(l)):
#         if type(l[q]) != list:
#             temp.append(l[q])
#         else:
#             temp += sp(l[q])
#     return temp
# print(sp(l))
def rec(l):
    tmp_sp = []
    for q in l:
        tmp_sp += rec(q) if isinstance(q, list) else [q]
    return tmp_sp
print(rec(l))