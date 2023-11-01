x = list(input())
sum  = 0

code = {'A':10, 'J':18, 'S': 26, 'B': 11, 'K':19, 'T':27, 'C':12, 'L':20, 'U':28, 'D':13, 
'M':21, 'V':29, 'E': 14, 'N':22, 'W':32, 'F':15, 'O':35, 'X':30, 'G':16, 'P':23, 'Y':31, 
'H':17, 'Q':24, 'Z':33, 'I':34, 'R':25}


a = x.pop(0)
abc = list(str(code[a]))
sum += (int(abc[0]) + int(abc[1]) * 9)

for i in range(0, 8):
    sum += int(x[i]) * (8-i)

sum += int(x[8])

if sum % 10 == 0:
    print("real")
else:
    print("fake")