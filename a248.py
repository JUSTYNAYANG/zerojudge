# not done
while True:
    try:
        a, b, c = input().split()

        out = int(a)/int(b)
        c = int(c)
        print(f"{out:.{c}f}")
    except:
        break

