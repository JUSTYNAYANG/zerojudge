# def f(n):
#     sum = n
#     for i in range(1, n):
#         sum += i
#     return sum

# def g(n):
#     sum = 0
#     for i in range(n):
#         sum += f(n-i)
#     return sum

# while True:
#     try:
#         a = int(input())
#         print(f(a), end=" ")
#         print(g(a))
#     except:
#         break


#f(n) = n + (n-1) ....+ 0
#g(n) = f(n)+f(n-1)....f(1)
while True:
    try:
        a = int(input())
        f = 0
        g = 0
        for i in range(1, a+1):
            f += i
            g += f
        print(f, g)
    except:
        break