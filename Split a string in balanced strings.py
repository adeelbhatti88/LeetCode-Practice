inputString = "RLRRRLLRLL"

def balancedStringSplit(s):
    stringToList = list(s)
    balanceVariable = 0
    answer = 0

    for i in range(len(stringToList)):
        if stringToList[i] == 'L':
            balanceVariable +=1
        else:
            balanceVariable -=1
        if balanceVariable == 0:
            answer +=1

    return answer


print(balancedStringSplit(inputString))