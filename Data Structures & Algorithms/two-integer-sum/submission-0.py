
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        i=0
        for n in nums:
            com=target-n
            if com in seen:
                return [seen[com],i]

            seen[n]=i
            i=i+1
