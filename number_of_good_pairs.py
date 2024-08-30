#https: //leetcode.com/problems/number-of-good-pairs/
from typing import Counter, List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0 
        counted = {}
        for num in nums:
            if num in counted:
                counted[num] +=1
            else:
                counted[num] = 1
        print(counted)
        for k,v in counted.items():
            count += v*(v-1) // 2
        return count
solution = Solution()
print(solution.numIdenticalPairs((1,2,3,34,5,1,2,3,1,5)))
