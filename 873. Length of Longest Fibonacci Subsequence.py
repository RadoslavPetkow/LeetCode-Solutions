class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        index = {num: i for i, num in enumerate(arr)}
        dp = {}
        max_length = 0

        for j in range(len(arr)):
            for i in range(j):
                prev = arr[j] - arr[i]
                if prev in index and index[prev] < i:
                    k = index[prev]
                    dp[(i, j)] = dp.get((k, i), 2) + 1
                    max_length = max(max_length, dp[(i, j)])
        
        return max_length if max_length >= 3 else 0
