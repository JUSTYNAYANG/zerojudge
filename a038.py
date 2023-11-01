a = int(input())
c = [0,0,0]

for i in range(a):
    b = int(input())
    if b % 3 == 0:
        c[0] += 1
    elif (b-1) % 3 == 0:
        c[1] += 1
    elif (b-2) % 3 == 0:
        c[2] += 1



print(f"{str(c[0])} {str(c[1])} {str(c[2])}")