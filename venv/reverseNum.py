num = 123


def ReverseNum(x):
    length = len(str(x))
    xToList = [int(x) for x in str(num)]
    print(xToList)
    i = 0
    z = length - 1
    while i < z:
        temp = xToList[i]
        xToList[i] = xToList[z]
        xToList[z] = temp
        i +=1
        z-=1
        # Converting integer list to string list
        s = [str(i) for i in xToList]

        # Join list items using join()
        res = int("".join(s))

        print(res)



ReverseNum(num)