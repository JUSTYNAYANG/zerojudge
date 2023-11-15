while True:
    try:
        n, m = input().split(" ")
        n = int(n)
        m = int(m)
        l = 0
        sum = 0
        while True:
            sum += n
            l += 1
            n += 1
            if sum > m:
                break
        print(l)
    except:
        break
