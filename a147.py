
while True:
    try:
        x = int(input())
        a = []
        for i in range(1, x):
            if i%7 != 0:
                a.append(str(i))
        if a:
            print(" ".join(a))
    except:
        break