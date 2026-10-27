class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        w = list(zip(position, speed))

        w.sort( key=lambda x : x[0])
        stk=[]
        c=0
        max=0

        for p,v in w[::-1]:
            time=(target-p)/v

            if time> max:
                c+=1
                max=time

        return c
