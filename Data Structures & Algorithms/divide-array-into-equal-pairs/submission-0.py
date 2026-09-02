class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # edge case
        if len(nums) < 1:
            return False
        # counter used here? if freq and value matches nums / n could work
        freq = Counter(nums)
        for count in freq.values():
            if count % 2 != 0:
                return False
        return True      