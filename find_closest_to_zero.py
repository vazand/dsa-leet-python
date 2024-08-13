from typing import List, Tuple


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        numsAbsValue: List[Tuple[int,int]] = list(map(lambda x: (abs(x), x), nums))
        numsAbsValue.sort(key = lambda x: x[0])
        print(numsAbsValue)
        closestToZero: int = numsAbsValue[0][0]
        print("closestToZero ",closestToZero)
        myarr: List[Tuple[int,int]] = []
        for i in range(0,len(numsAbsValue)):
            #for j in range(0,len(numsAbsValue[i])):
            if numsAbsValue[i][0] == closestToZero:
                myarr.append(numsAbsValue[i])
        print("myarr ",myarr)

        maxValue: int = myarr[0][1]
        for i in range(0,len(myarr)):
            #for j in range(0,len(myarr[i])):
            if myarr[i][1] > maxValue:
                maxValue = myarr[i][1]
        return maxValue

soln = Solution()
print(soln.findClosestNumber([-100000,-100000]))          

