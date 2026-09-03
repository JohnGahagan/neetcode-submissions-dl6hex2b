class Solution:
    def longestPalindrome(self, s: str) -> int:
        countLetters = Counter(s)
        length = 0
        has_odd = False

        for char,freq in countLetters.items():
            length += (freq // 2) * 2
            if freq % 2 == 1:
                has_odd = True
        if has_odd:
            length += 1
        return length