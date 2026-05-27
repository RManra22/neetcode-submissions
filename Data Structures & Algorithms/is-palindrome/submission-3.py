class Solution:
    def isPalindrome(self, s: str) -> bool:
        lettersNumbers = ['A','B','C','D',
                          'E','F','G','H',
                          'I','J','K','L',
                          'M','N','O','P',
                          'Q','R','S','T',
                          'W','V','Y','X',
                          'Z','1','2','3',
                          '4','5','6','7',
                          '8','9','0']

        string = list(s.upper())
        arr = []
    
        for char in string:
            if char in lettersNumbers:
                arr.append(char)
        
        l = 0
        r = len(arr) - 1
        while l < r: 
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True
        