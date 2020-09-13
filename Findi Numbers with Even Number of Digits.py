nums = [12,345, 2,6,7896]


# print(len(str(nums[0])))

evenNums = 0
for i in range(len(nums)):
    if len(str(nums[i])) % 2 == 0:
        evenNums +=1


print(evenNums)