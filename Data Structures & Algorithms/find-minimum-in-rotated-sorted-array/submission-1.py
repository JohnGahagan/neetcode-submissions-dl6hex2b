class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # Min is in the right half (excluding mid)
                l = mid + 1
            else:
                # Min is in the left half (including mid)
                r = mid

        return nums[l]  # l == r, pointing at the minimum