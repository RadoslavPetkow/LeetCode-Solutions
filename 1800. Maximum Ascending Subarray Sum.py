nums = [12,17,15,13,10,11,12]
inc_len = nums[0]
max_len = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:  # Increasing
        inc_len += nums[i]
    else:  # Neither increasing nor decreasing
        inc_len = nums[i]
    if inc_len > max_len: max_len = inc_len

print(inc_len)
