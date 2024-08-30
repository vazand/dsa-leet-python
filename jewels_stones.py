# https://leetcode.com/problems/jewels-and-stones/description/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jh = {elem: 1 for idx, elem in enumerate(jewels)}
        count = 0
        for i in range(len(stones)):
            if stones[i] in jh:
                count += 1
        return count
