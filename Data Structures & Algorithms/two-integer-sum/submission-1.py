
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
      
        for i,n in enumerate(nums):
            com=target-n
            if com in seen:
                return [seen[com],i]

            seen[n]=i
        
