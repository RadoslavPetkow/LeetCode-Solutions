boxes = "001011"
result = []
boxes = [x for x in boxes]

for i in range(len(boxes)):
    item = 0
    for j in range(len(boxes)):
        if j != i and boxes[j] == "1":
            item += abs(i-j)
    result.append(item)

print(result)

"""
CHATGPT SOLVE
class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        result = [0] * n
        moves = 0
        count = 0
        for i in range(n):
            result[i] += moves
            count += int(boxes[i])
            moves += count
        moves = 0
        count = 0
        for i in range(n-1, -1, -1):
            result[i] += moves
            count += int(boxes[i])
            moves += count
        return result
"""
