from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result= Counter(nums)

        final= [ key for key,counter in result.most_common(k)]

        return final

        
        