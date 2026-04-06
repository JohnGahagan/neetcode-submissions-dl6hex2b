class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1 + nums2)
        num1count = len(nums1)
        num2count = len(nums2)
        
        if len(combined) % 2 == 0:
            while len(combined) > 2:
                combined.pop(len(combined)-1)
                combined.pop(0)
            eventotal = (combined[0] + combined[1]) / 2.0
            return float(eventotal)
        else:
            while len(combined) > 1:
                combined.pop(len(combined)-1)
                combined.pop(0)
            oddtotal = combined[0]
            return float(oddtotal)