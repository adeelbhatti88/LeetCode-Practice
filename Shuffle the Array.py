nums = [2,5,1,3,4,7]
answerList= []
n = 3
i = 0

for i in range(int((len(nums)/ 2))):
    answerList.append(nums[i])
    answerList.append(nums[i + n])
    i+=1


print(answerList)
