class Solution:
    def isValid(self, s: str) -> bool:
        seen=[]
        check={")":"(","]":"[","}":"{"}

        for c in s:
            if c in check:
                top=seen.pop() if seen else "*"
                if top!=check[c]:
                    return False
            else:
                seen.append(c)

        return not seen