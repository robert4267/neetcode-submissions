class Solution:
    def isValid(self, s: str) -> bool:
        seen= []
        check={")":"(","]":"[","}":"{"}
        for c in s:
            if c in check:
                top_elem= seen.pop() if seen else "*"

                if check[c] != top_elem:
                    return False
            else:
                seen.append(c)

        return not seen