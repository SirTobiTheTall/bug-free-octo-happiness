from random import randint

n = 100
a = []

for i in range(n):

    a.append(randint(1,6))

b = sum(a)/n

#print(a)
print(b)
