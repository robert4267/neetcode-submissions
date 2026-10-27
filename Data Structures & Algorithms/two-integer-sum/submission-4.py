class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t=0
        a=0
        b=0
        for i,nr in enumerate(nums):
            t = target-nr
            if t in nums[i+1:]:
                a=nr
                b=i
                break
        return [ nums.index(a),nums.index(t,b+1)]