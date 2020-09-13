# num = 121
#
# numList = list(map(int, str(num)))
# originalList = numList
#
# print(numList)
#
# i = 0
# z = len(numList) - 1
#
# while i < z:
#     temp = numList[i]
#     numList[i] = numList[z]
#     numList[z] = temp
#     i+=1
#     z-=1
#
# if originalList == numList:
#     print("true")
# else:
#     print("false")

x = -123
num = abs(x)
numList = list(map(int, str(num)))
numList = -numList

print(numList)

# isnegative = False
# if x < 0:
#     isnegative = True
# num = abs(x)
# numList = list(map(int, str(num)))
# originalList = numList
#
# i = 0
# z = len(numList) - 1
#
# while i < z:
#     temp = numList[i]
#     numList[i] = numList[z]
#     numList[z] = temp
#     i += 1
#     z -= 1
#
# if originalList == numList and isnegative == True:
#     print('false')
# elif originalList == numList and isnegative == False:
#     print('true')
# else:
#     print('false')
