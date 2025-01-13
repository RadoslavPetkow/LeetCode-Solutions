class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)

        result = 0

        while dividend >= divisor:
            temp_divisor, num_shifts = divisor, 0
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_shifts += 1
            dividend -= temp_divisor
            result += 1 << num_shifts

        if negative:
            result = -result

        return max(INT_MIN, min(INT_MAX, result))