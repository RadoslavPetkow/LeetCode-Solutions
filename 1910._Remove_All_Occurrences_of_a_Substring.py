class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while True:
            if part in s:
                s = re.sub(part, "", s, count=1)
            else:
                break
        return s
