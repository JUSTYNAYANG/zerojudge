import math
num = int(input())
d = []
k = 0

for i in range(num):
    a = int(input())
    b = int(input())
    sum = 0
    for i in range(a, b):
        if math.sqrt(i)%1 == 0:
            sum += i
    d.append(f"Case {1+k}: {sum}")
    k += 1

for i in d:
    print(i)
