from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        t = []
        for x in nums:
            if c[x] == 2:
                t.append(x)
        return set(t)
            
