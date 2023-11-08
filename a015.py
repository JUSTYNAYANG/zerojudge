while True:
    try:
        row, column = input().split()
        x = []

        for i in range(int(row)):
            x.append(input().split())

        for i in range(int(column)):
            a = []
            for j in range(int(row)):
                a.append(f"{x[j][i]}")
            print(" ".join(a))
    except:
        break