class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        smallWord = min(len(word1),len(word2))
        print("smallWord",smallWord)
        conCatStr :str = ""
        for chi,chj in zip(word1,word2):
            conCatStr = conCatStr+ chi +chj
        print("result",conCatStr)
        if len(word1) > len(word2):
            for cho in range(len(word2),len(word1)):
                conCatStr = conCatStr + word1[cho]
        elif len(word1) < len(word2):
            for cho in range(len(word1),len(word2)):
                conCatStr = conCatStr + word2[cho]
        print("final",conCatStr)
        return conCatStr

solution = Solution()
print(solution.mergeAlternately("ab","pqrs"))