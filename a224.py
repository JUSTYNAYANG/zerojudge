
#not done
# def f(a, b):
#     aa = "".join(a).lower()
#     bb = "".join(b).lower()
#     if "".join(a).lower() == "".join(b).lower():
#         print("yes !")
#     else:
#         print("no...")

# l = list("abcdefghijklmnopqrstuvwxyz")
# while True:
#     try:
#         a = list(input())
#         if a == []:
#             break
#         else:
#             for i in a:
#                 if i not in l:
#                     a.remove(i)
#             b = a.copy()
#             b.reverse()
#             f(a, b)

#     except:
#         break
        



# l = list("abcdefghijklmnopqrstuvwxyz")
# while True:
#     try:
#         a = list(input())
#         b = set(a)
#         c = 0
#         if a == []:
#             break
#         else:
#             for i in b:
#                 if i not in l:
#                     a.remove(i)
#                 elif  i == "_":
#                     a.remove("_")
#                 elif a.count(i)%2 != 0:
#                     c += 1
#             print(a)
#             if c >= 1:
#                 print("no...")
#             else:
#                 print("yes !")
#     except:
#         break
        


while True:
    try:
        a = list(input())
        if a == []:
            break
        b = set(a)
        c = 0
        l = "abcdefghijklmnopqrstuvwxyz"
        for i in b:
            if i in l:
                o = a.count(i)
                if o%2 != 0:
                    c += 1
        if c >= 1:
            print("no...")
        else:
            print("yes !")
    except:
        break
