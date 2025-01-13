from datetime import date


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        given_date = date(year, month, day)
        return given_date.strftime("%A")
