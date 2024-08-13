class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x 
        while start <= end:
            middle = (start + end)//2
            if middle * middle ==  x:
                return middle
            elif middle * middle < x:                    
                start = middle+1
            elif middle * middle > x:
                end = middle -1
        return end
        
solution = Solution()
print(solution.mySqrt(3))