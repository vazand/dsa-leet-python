from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lt = list(t)
        ls = list(s)
        sh: int = 0
        th: int = 0
        bool = True
        while sh < len(ls) and bool:
            while th < len(lt):
                if(sh == len(ls)-1):
                    bool = False
                elif(ls[sh] == lt[th]):
                    print("If th ", th)
                    print("If sh ", sh)
                    sh = sh+1
                    th = th+1
                    print(True)
                else:
                    print("else sh ", sh)
                    th=th+1

solution = Solution()
print(solution.isSubsequence("abc","ahbgdcdfadfa"))
