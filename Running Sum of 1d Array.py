nums = [1,2,3,4]
answerList = []
counter = 0

i = 1
while i<len(nums):

    nums[i]+=nums[i-1]
    i+=1


print(nums)