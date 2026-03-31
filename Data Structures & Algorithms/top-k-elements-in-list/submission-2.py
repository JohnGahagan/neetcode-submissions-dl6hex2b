class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = Counter(nums)
            ans = []
            for item, k in count.most_common(k):
                ans.append(item)
            return ans