class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i,nr in enumerate(nums):
            t= target-nr
            if t in seen:
                return [ seen[t],i ]

            
            seen[nr]=i

        return []