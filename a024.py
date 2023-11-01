#version 1
j = 0
n = input().split()
a = int(n[0])
b = int(n[1])
n.sort()
for i in range(1, min(a, b)):
    if a % i == 0 and b % i == 0:
        j = i
print(j)

#version 2
out = 1
a = input().split()
for i in range(1, min(int(a[0]), int(a[1]))):
    if int(a[0]) % i == 0:
        if int(a[1]) % i == 0:
            out = i

print(out)

#version 3
import math
n = input().split()
print (math.gcd(int(n[0]), int(n[1])))


