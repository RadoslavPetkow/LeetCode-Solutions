from math import factorial

class Solution(object):
    def getPermutation(self, n, k):
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1
        result = []

        for i in range(n):
            fact = factorial(n - 1 - i)
            index = k // fact
            result.append(numbers.pop(index))
            k %= fact

        return ''.join(result)