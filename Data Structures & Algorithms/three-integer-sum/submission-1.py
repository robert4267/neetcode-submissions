from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            curr = nums[i]
            
            if curr > 0:
                break
                
            if i > 0 and curr == nums[i - 1]:
                continue
                

            if curr + nums[n - 2] + nums[n - 1] < 0:
                continue
                

            if curr + nums[i + 1] + nums[i + 2] > 0:
                break  
                
            j = i + 1
            k = n - 1
            
            while j < k:
                total = curr + nums[j] + nums[k]
                
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([curr, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                        
        return res
