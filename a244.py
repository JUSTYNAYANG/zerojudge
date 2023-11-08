import math
x = int(input())
for i in range(x):
    a = input().split()
    if a[0] == "1":
        print(int(a[1]) + int(a[2]))
    elif a[0] == "2":
        print(int(a[1]) - int(a[2]))
    elif a[0] == "3":
        print(int(a[1]) * int(a[2]))
    elif a[0] == "4":
        print(math.floor(int(a[1]) / int(a[2])))

