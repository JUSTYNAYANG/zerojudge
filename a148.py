while True:
    try:
        a = input().split(" ")
        sum = 0
        for i in range(int(a[0])):
            sum += int(a[i+1])

        sum = sum/int(a[0])
        if sum > 59:
            print("no")
        else:
            print("yes")
    except:
        break

