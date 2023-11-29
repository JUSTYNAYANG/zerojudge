# while True:
#     try:
#         answer = input().split()

#         l = int(input())
#         for i in range(l):
#             A = 0
#             B = 0
#             an = []
#             te = []
#             test = input().split()
#             for j in range(4):
#                 if test[j] == answer[j]:
#                     A += 1
#                 else:
#                     an.append(answer[j])
#                     te.append(test[j])
            
#             for j in te:
#                 if j in an:
#                     B += 1
            
#             print(f"{A}A{B}B")
#     except:
#         break

# def checker(answer, test):
#     A = 0
#     B = 0
#     an = []
#     te = []
#     for j in range(4):
#         if test[j] == answer[j]:
#             A += 1
#         else:
#             an.append(answer[j])
#             te.append(test[j])
    
#     for j in te:
#         if j in an:
#             B += 1
    
#     return f"{A}A{B}B"

# while True:
#     try:
#         answer = input().split()

#         l = int(input())
#         for i in range(l):
#             test = input().split()
#             print(checker(answer, test))
#     except:
#         break