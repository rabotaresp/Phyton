h = 'helloh python'
# d = 'hello'
# #Task 1
# #1
# print(h[2])
# #2
# print(h[10])
# #3
# print(h[slice(5)])
# #4
# print(h[slice(0, 10)])
# #5
# print(h[slice(0, 12, 2)])
# #6
# print(h[slice(1, 12, 2)])
# #7
# print(h[::-1])
# #8
# r = h[::-1]
# print(r[slice(0, 12, 2)])
# #9
# print(len(h))
# #Task 2
# print(h.count(' ')+1)
# #Task3
# print(len(d))
# if len(d)%2 == 0:
#     part1 = (d[slice(0, len(d)//2)])
#     part2 = d[slice(len(d)//2, len(d))]
#     print(part2,part1)
# elif len(d)%2 != 0:
#     part1 = d[slice(0, (len(d)//2)+1)]
#     part2 = (d[slice(((len(d) // 2)+1), len(d))])
#     print(part2,part1)
# #Task4
# sp = h.split(' ')
# print(sp[1], sp[0])
#Task5
# if h.find('f')!= -1:
#     print(h.find('f'))
#     print(h.rfind('f'))
# elif h.find('f')== -1:
#     print()
#Task6
# sp = h.split(' ')
# if sp[0].find('f')!=-1 and sp[0].rfind('f')!=-1:
#     print(sp[0].rfind('f')+1)
# if sp[1].find('f')!=-1 and sp[1].rfind('f')!=-1:
#     print(sp[1].rfind('f') + 1)
# if sp[0].find('f')==-1 and sp[1].rfind('f')==-1:
#     print(-2)
# if sp[0].find('f')!=-1 and sp[1].rfind('f')==-1 or sp[0].find('f')==-1 and sp[1].rfind('f')!=-1:
#     print(-1)
#Task 7
# p=list(h)
# for q in range (h.find('h'), h.rfind('h')+1):
#     p.pop(h.find('h'))
#     print(p)
#Task8
# print(h[h.rfind('h'): h.find('h'):-1])
#Task9
# h = '1 two three four five'
# print(h.replace('1','one'))
#Task10
# p=list(h)
# for q in range(len(p)):
#     if (q+1)%3==0:
#         p.pop(q)
#         print(p)
#Task11
# h = '@fadfjad @ n df'
# print(h.replace('@',''))
#Task12
p=h.replace('h','H')
sp = p.split(' ')
for q in range (len(p)):
    if sp[0].find('H')!=-1 and p[q]=='H' and sp[1].rfind('H')!=-1:
        sp[0][p.find('H')]='h'
        p[p.rfind('H')]='h'
        print(x+y)
    break
