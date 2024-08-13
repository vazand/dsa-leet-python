from typing import List, Tuple


class Solution:
    def romanToInt(self, s: str) -> int:
        romanAndIntGroup: List[Tuple[chr, int]] = [
            ("M", 1000),
            ("D", 500),
            ("C", 100),
            ("L", 50),
            ("X", 10),
            ("V", 5),
            ("I", 1),
        ]
        refList: List[int] = []
        for i in s:
            for j in romanAndIntGroup:
                if i == j[0]:
                    refList.append(j[1])
        print("ref list", refList)
        sum: int = 0
        num: int = 0
        if len(refList) == 1:
            return refList[0]
        while num < len(refList) -1:
            print("runner num:", num)
            if refList[num] < refList[num+1]:
                print("in IfCond sum before", sum)
                sum = sum + (refList[num+1] - refList[num])
                print("in IfCond sum after", sum)
                num = num + 2
            else:
                print("In else cond", refList[num])
                print("in elseCOnd sum before", sum)
                sum = sum+refList[num]
                print("in elseCOnd sum after", sum)
                num = num + 1
            if num == len(refList)-1:
                sum = sum+ refList[num]
        return sum



solution = Solution()
# solution.romanToInt("MCMIX")
print(solution.romanToInt("D"))
