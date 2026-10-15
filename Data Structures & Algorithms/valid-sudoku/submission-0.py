from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # --- PASS 1: ROWS ---
        for i in range(9):
            seen = list()  # Reset empty list for each new row
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if val in seen: 
                        return False
                    seen.append(val)

        for j in range(9):
            seen2 = list()
            for i in range(9):
                val = board[i][j]
                if val != ".":
                    if val in seen2: 
                        return False
                    seen2.append(val)

        for i in range(0, 9, 3): 
            for j in range(0, 9, 3):
                seen3 = list()  
                
                for r in [i, i+1, i+2]:
                    for c in [j, j+1, j+2]:
                        val = board[r][c]
                        if val != ".":
                            if val in seen3: 
                                return False
                            seen3.append(val)
                            
        return True
