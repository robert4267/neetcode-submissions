class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output= [1] * len(nums)
        ltotal=1
        for i in range(len(nums)):
            output[i]= ltotal
            ltotal*=nums[i]

        rtotal=1
        for i in range(len(nums)-1,-1,-1):
            output[i] *=rtotal
            rtotal *=nums[i]
            

        return output                