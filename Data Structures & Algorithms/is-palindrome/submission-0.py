class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
            
        reversed_cleaned = ""
        for char in cleaned:
            reversed_cleaned = char + reversed_cleaned
        return reversed_cleaned == cleaned
            