from random import randint
import sys

n = int(sys.argv[1])

a = []

for i in range(n):

    a.append(randint(1,6))

b = sum(a)/n

print(a)
print(b)
