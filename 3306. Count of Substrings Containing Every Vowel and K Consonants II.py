class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        vowels = set("aeiou")
        n = len(word)
        count = 0
        
        for start in range(n):
            vowel_freq = {v: 0 for v in vowels}
            total_consonants = 0
            
            for end in range(start, n):
                ch = word[end]
                if ch in vowels:
                    vowel_freq[ch] += 1
                else:
                    total_consonants += 1  
                
                if all(vowel_freq[v] > 0 for v in vowels):
                    if total_consonants == k:
                        count += 1
                    elif total_consonants > k:
                        break
        
        return count
