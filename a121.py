#TLE not completed
import math
def isPrime(n):
    p = str(n).split()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        c, d = input().split()
        a = 0
        for i in range(int(c), int(d)+1):
            if i > 10 and i % 10 in (2, 4, 5, 6, 8):
                continue
            if isPrime(i):
                a += 1
        print(a)
    except:
        break