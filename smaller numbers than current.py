nums = [8,1,2,2,3]
numCount = []
count = 0
for i in nums:
    count = 0
    for z in nums:
        if z < i:
            count +=1

    numCount.append(count)

print(numCount)