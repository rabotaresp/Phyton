# f = open('file.txt', 'w')
# f.write('Some text')
# f.close()
# print(f)
# f = open('file.txt')
# text = f.read()
# print(text)
# f.close()
res_sp = []
with open('file.txt') as f:
    for line in f:

        l = line.lower().split()
        for q in l:
            if q.endswith('.exe'):
                res_sp.append(q)
for q in res_sp:
    print(q)