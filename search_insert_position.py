import math
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if target > nums[end]:
            return len(nums)
        elif target < nums[start]:
            return start
        else:
            while start <= end:
                middle = math.floor((start+end)/2)
                if target == nums[middle]:
                    return middle
                elif target > nums[middle]:
                    if target < nums[middle + 1]:
                        return middle + 1
                    start = middle + 1
                elif target < nums[middle]:
                    end = middle - 1


solution = Solution()

print(solution.searchInsert((1, 3, 5), 4))
print(solution.searchInsert((1, 3, 5, 6), 5))
print(solution.searchInsert((1, 3, 5, 6), 2))
print(solution.searchInsert((1, 3, 5, 6), 7))
print(solution.searchInsert((1, 3, 5, 8,9), 7))
