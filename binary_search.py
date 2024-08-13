from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1
        middle = (start + end) // 2
        while start <= end:
            print(nums[middle])
            middle = (start + end) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                start = middle + 1
            elif target < nums[middle]:
                end = middle - 1
        return -1


solution = Solution()
print(solution.search((10,11,12,13,14,15,16,17),18))