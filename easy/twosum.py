
nums = [2,7,11,15]
target = 9

outList = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j: pass
        elif nums[i] + nums[j] == target:
            outList.append(i) 
            outList.append(j) 
            print(outList)
            breakI = True
            break

    if breakI: break



