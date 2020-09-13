nums = [0,1,2,3,4]
index = [0,1,2,2,1]

AnswerList = []

for i in range(len(nums)):
    AnswerList.insert(index[i], nums[i])

print(AnswerList)

