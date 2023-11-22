
while True:
    try:
        a = list(input())
        c = 0
        if a == []:
            break
        else:
            s = []
            for i in a:
                if i.isalpha():
                    s += i.lower()

        o = set(s)
        for i in o:
                if s.count(i)%2 == 1:
                    c += 1
        
        if c > 1:
                print("no...")
        else:
                print("yes !")
    except:
         break
        