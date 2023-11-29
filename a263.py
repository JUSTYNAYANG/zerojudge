from datetime import datetime, timedelta

while True:
    try:
        a = input().split()
        b = input().split()

        for i in range(3):
            a[i] = int(a[i])
            b[i] = int(b[i])
        d = datetime(a[0], a[1], a[2]) - datetime(b[0], b[1], b[2])

        print(abs(d.days))
    except:
        break