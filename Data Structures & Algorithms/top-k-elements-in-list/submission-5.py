class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}
        freq = [ [] for x in range(len(nums)
        +1)]

        for nr in nums:
            count[nr] = 1 + count.get(nr,0)

        for n,c in count.items():
            freq[c].append(n)

        res=[]

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
