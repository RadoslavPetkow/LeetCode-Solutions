class Solution:
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx, dy = x1 - x0, y1 - y0

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y - y0) * dx != (x - x0) * dy:
                return False

        return True