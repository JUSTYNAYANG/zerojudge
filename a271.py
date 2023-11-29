def rabbit():
    data = input().split()
    x = int(data[0])
    y = int(data[1])
    z = int(data[2])
    w = int(data[3])
    n = int(data[4])
    m = int(data[5])
    data = input().split()
    poison = 0
    for i in data:
        m -=poison * n
        if m <= 0:
            print("bye~Rabbit")
            break

        if i=='1':
            m += x
        elif i=='2':
            m += y
        elif i=='3':
            m -= z
        elif i=='4':
            m -= w
            poison += 1
        if m <= 0:
            print('bye~Rabbit')
            break
    if m>0:
        print(f"{m}g")

count = int(input())
for i in range(count):
  rabbit()

