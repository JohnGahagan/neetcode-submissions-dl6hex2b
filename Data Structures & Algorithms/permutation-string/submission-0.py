class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = sorted(s1)
        window_size = len(s1)

        for start in range(len(s2) - window_size + 1):
            window = s2[start : start + window_size]
            if sorted(window) == target:
                return True
        return False