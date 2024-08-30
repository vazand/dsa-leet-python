# https: //leetcode.com/problems/permutation-difference-between-two-strings/
import math


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ta = list(t)
        sh = {ele: idx for idx, ele in enumerate(s)}
        sum = 0
        for i in range(len(ta)):
            if ta[i] in sh:
                print(i,"",ta[i])
                sum += abs(sh.get(ta[i])-i)
        
        
        # th = {ele: idx for idx, ele in enumerate(t)}
        # #formula = math.abs(a,b)
        # sum = 0
        # for key1 in sh:
        #     if key1 in th:
        #        sum += abs(sh.get(key1) - th.get(key1))
        # print(sh)
        # print(th)
        return sum
solution = Solution()
s = "abc"
t="bac"
print(solution.findPermutationDifference(s,t))
