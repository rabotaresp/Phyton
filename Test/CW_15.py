# l = zip([-2,-5,-2],[1,2,3],['a','b','c'])
# for q in l:
#     print(q)

def f(x):
    return x*x
nums = [1, 2, 3]
for num in nums:
    print (f(num))
def f(x):
    return x * x
print([f(num)for num in nums])
def f(x, y):
    return x*y

a = [1,3,4]
b = [3,4,5]
y = list(map(f, a, b))
print (y)
[3, 12, 20]