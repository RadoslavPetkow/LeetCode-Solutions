nums = [3,4,5,1,2]

for i in range(len(nums)):
    if nums == sorted(nums):
        print(True)
        exit(0)

    nums.append(nums[0])
    nums.pop(0)

print(False)