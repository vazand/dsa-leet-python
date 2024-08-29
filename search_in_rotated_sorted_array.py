from typing import List


class Solution:
    def search(self, nums: List[int], t: int) -> int:
        s = 0
        e = len(nums) - 1
        while s<=e:
            mid = (s+e)//2
            if nums[mid] == t:
                return mid
            # left sorted array
            if nums[s] <= nums[mid]:
                if t > nums[mid]:
                    s = mid+1
                else: # t< nums[mid]
                    if t < nums[s]:
                        s = mid+1
                    else:
                        e = mid-1
            else:
                if t < nums[mid]:   
                    e = mid-1
                elif t > nums[e]:
                    e = mid-1
                else:
                    s= mid+1
        return -1

solution = Solution()
print(solution.search((4,5,0,1,2),5))
