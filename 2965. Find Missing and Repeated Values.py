class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        n_squared = n * n
        count = [0] * (n_squared + 1)
        
        for row in grid:
            for num in row:
                count[num] += 1
        
        repeated = -1
        missing = -1
        
        for i in range(1, n_squared + 1):
            if count[i] == 2:
                repeated = i
            elif count[i] == 0:
                missing = i
        
        return [repeated, missing]
