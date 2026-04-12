class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = len(nums) - 1
        l = 0
        
        max_reach = 0
        
        for i in range(len(nums)):
            # if we can't even reach this index, we're stuck
            if i > max_reach:
                return False
            
            # update how far we can go
            max_reach = max(max_reach, i + nums[i])
            
            # early success
            if max_reach >= r:
                return True
        
        return True