class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        w = list(zip(position, speed))

        w.sort( key=lambda x : x[0])
        stk=[]

        for p,v in w[::-1]:
            stk.append((target-p)/v)

            if len(stk)>=2 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)
