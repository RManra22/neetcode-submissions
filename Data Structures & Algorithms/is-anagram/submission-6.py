class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s) != len(t):
            return False

        word1 = list(s)
        word2 = list(t)

        word1.sort()
        word2.sort()

        return word1 == word2
