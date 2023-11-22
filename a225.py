# # not done

# # r = int(input())
# # b = []

# # num = input().split(" ")
# # for i in num:
# #     o = list(i)[::-1]
# #     b.append("".join(o))

# # b.sort()

# # for i in range(len(b)):
# #     b[i] = b[i][::-1]
# # print(b)

# # r = int(input())
# mke
# while True:
#     try:
#         p = input()
#         b = []
#         c = []

#         num = input().split(" ")
#         for i in num:
#             o = list(i)
#             for i in range(len(o)):
#                 o[i] = int(o[i])
#             b.append(o)

#         if len(o) == 1:
#             b.sort()
#         else:
#             b.sort(key = lambda y : (y[1], -y[0]))

#         for i in b:
#             for j in range(len(i)):
#                 i[j] = str(i[j])
#             c.append("".join(i))

#         print(" ".join(c))
#     except:
#         break

while True:
    try:
        x = input()
        y = input().split()
        u = sorted (y, key=lambda z: (int(z[-1]), -int(z)))
        print (*u, sep=' ')
    except:
        break