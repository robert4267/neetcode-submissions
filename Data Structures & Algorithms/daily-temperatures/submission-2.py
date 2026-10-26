class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res= [0] * n 

        stk=[]
        stk_append = stk.append
        stk_pop = stk.pop

        for i,temp in enumerate(temperatures):
            while stk and temp > temperatures[stk[-1]]:
                prev_id=stk_pop()
                res[prev_id]=i-prev_id
            stk_append(i)

        return res