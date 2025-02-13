from collections import defaultdict


def maximumSum(nums):
    groups = defaultdict(list)
    for num in nums:
        digit_sum = sum(int(digit) for digit in str(num))
        groups[digit_sum].append(num)

    max_pair_sum = -1
    for digit_sum, values in groups.items():
        if len(values) >= 2:
            values.sort(reverse=True)
            candidate = values[0] + values[1]
            max_pair_sum = max(max_pair_sum, candidate)

    return max_pair_sum
