class Solution:
    def specialArray(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for x in range(n+1):
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
            if count == x:
                return count       
        return -1