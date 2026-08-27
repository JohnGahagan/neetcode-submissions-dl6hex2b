from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)    
        window_counts = {}        
        required = len(need)       
        formed = 0                

        best_len = float('inf')
        best_left = 0
        left = 0

        for right, char in enumerate(s):
            if char in need:
                window_counts[char] = window_counts.get(char, 0) + 1
                if window_counts[char] == need[char]:
                    formed += 1   
            while formed == required:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_left = left
                left_char = s[left]
                if left_char in need:
                    window_counts[left_char] -= 1
                    if window_counts[left_char] < need[left_char]:
                        formed -= 1   
                left += 1

        return "" if best_len == float('inf') else s[best_left : best_left + best_len]