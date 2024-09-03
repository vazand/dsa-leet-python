from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        si = 0
        tj = 0
        se = len(ls)-1
        te = len(lt)-1
        #print(len(ls))
        if se > te:
            return False
        if not ls:
            return True
        while si <= se:
            while tj <= te:
                if ls[si] == lt[tj]:
                    if si == se:
                        return True
                    if tj == te:
                        return False
                    print("if si ", ls[si])
                    print("if tj ", lt[tj])
                    si +=1
                    tj +=1
                    
                else:
                    if tj == te:
                        return False
                    print("else si ", ls[si])
                    print("else tj ", lt[tj])
                    tj +=1
        return False           
solution = Solution()
print(solution.isSubsequence("axc", "ahbgdc"))
