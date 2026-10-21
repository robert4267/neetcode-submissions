class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefix=[0]*n
        suffix=[0]*n
    
        pc=0
        for i in range(len(height)):
            prefix[i]=pc

            if height[i]>pc:
                pc=height[i]

        sc=0
        for i in range(len(height)-1,-1,-1):
            suffix[i]=sc

            if height[i]>sc:
                sc=height[i]


        total=0
        for i in range(len(height)):
            if min(prefix[i],suffix[i])-height[i]<=0:
                continue
            else:

                total=total+min(prefix[i],suffix[i])-height[i]
    

        return total
