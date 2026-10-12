class Solution:
    def hasDuplicate(self, nums: List[int]) :
        seen=list()
        for nr in nums:
            if nr in seen:
                return True
            seen.append(nr)
        return False
             