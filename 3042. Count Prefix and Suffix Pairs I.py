class Solution(object):
    def countPrefixSuffixPairs(self, words):
        result = 0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if i != j and words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    result += 1
        return result