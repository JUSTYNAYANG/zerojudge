a = int(input())

for i in range(a):
    b = list(input())
    sum = int(b[0])
    for j in range(len(b)-1):
        sum *= int(b[j+1])
    print(sum)