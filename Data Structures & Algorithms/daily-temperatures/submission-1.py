class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res= [0] * n 

        stk=[]

        for i,temp in enumerate(temperatures):
            while stk and temp > temperatures[stk[-1]]:
                prev_id=stk.pop()
                res[prev_id]=i-prev_id
            stk.append(i)

        return res