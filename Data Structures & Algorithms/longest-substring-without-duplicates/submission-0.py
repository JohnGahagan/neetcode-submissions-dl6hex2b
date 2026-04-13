class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res1 = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in res1:
                res1.remove(s[l])
                l += 1
            res1.add(s[r])
            res = max(res,r-l+1)
        return res
    