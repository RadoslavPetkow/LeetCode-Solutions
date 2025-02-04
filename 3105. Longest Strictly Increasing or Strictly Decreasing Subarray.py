def longestMonotonicSubarray(nums):
    if not nums:
        return 0

    inc_len = dec_len = max_len = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:  # Increasing
            inc_len += 1
            dec_len = 1  # Reset decreasing
        elif nums[i] < nums[i - 1]:  # Decreasing
            dec_len += 1
            inc_len = 1  # Reset increasing
        else:  # Neither increasing nor decreasing
            inc_len = dec_len = 1

        max_len = max(max_len, inc_len, dec_len)

    return max_len