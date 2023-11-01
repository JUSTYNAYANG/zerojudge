while True:
    try:
        a = input()

        b = input().split()

        for i in range(len(b)):
            b[i] = int(b[i])

        b.sort()

        for i in range(len(b)):
            b[i] = str(b[i])

        print(" ".join(b))
    except:
        break