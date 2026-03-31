class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversedStr = ""
        for c in s:
            if c.isalnum():
                reversedStr += c.lower()
        return reversedStr == reversedStr[::-1]

        
            