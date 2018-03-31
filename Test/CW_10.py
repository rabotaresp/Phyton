#1
# a = [1,2,3,4,5,6,7,8,9,10]
# for q in range (0, len(a),2):
#     print(a[q])
#2
# a = [1,2,3,4,5,6,7,8,9,10,12]
# for q in a:
#     if q%2 == 0:
#         print(q)
#3
# a = [1,12,3,11,24,3,6,7,4]
# for q in range (0, len(a)):
#     if a[q] > a[q-1]:
#         print(a[q])
#4
# a = [1,12,3,-11,24,-3,-6,-7,4,-1]
# for q in range (0, len(a)):
#     if a[q] * a[q-1]>0:
#         print(a[q], a[q-1])
#     if a[q] * a[q-1]>0 and a[q] * a[q+1]>0:
#         print(a[q])
#5
# a = [1,12,3,11,24,3,6,7,4]
# b = []
# for q in range (1, len(a)-1):
#     if a[q-1] < a[q] and a[q] > a[q+1]:
#         b.append(a[q])
# print(len(b))
#6
# a = [1,12,3,11,24,3,6,7,4]
# print(max(a))
# print(a.index(max(a)))
#7
# a = [180,200,156,156,145,120,118]
# x = int(input('Введите рост Пети: '))
# a.append(x)
# y=[]
# y = a.sort()
# print(a)
# for q in range(len (a)):
#     if x < a[q]:
#         print(q)
#         break
#8
# a = [1,2,3,4,5,6,7,8,9,10,11]
# y=[]
# y = a.sort()
# print(a)
# count = 1
# for q in range (len(a)-1):
#     if a[q] != a[q+1]:
#         count+=1
# print(count)
#9
# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# tmp = []
# for q in range (0,(len(a)-1),2):
#     tmp= a[q]
#     a[q]=a[q+1]
#     a[q+1]=tmp
# print(a)
#10
# a = [1,12,3,11,24,3,6,7,4]
# print(max(a))
# print(min(a))
# temp = max(a)
# tmp = (a.index(max(a)))
# a[tmp]=min(a)
# a[(a.index(min(a)))]= temp
# print(a)
#11
