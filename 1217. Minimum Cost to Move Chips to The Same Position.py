class Solution:
    def minCostToMoveChips(self, position):
        even_count = sum(1 for p in position if p % 2 == 0)
        odd_count = sum(1 for p in position if p % 2 == 1)

        return min(even_count, odd_count)