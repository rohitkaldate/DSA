class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # for i in range(len(words)):
        #     for j in range(i):
        #         if x in words[i] and words[j]:
        #             return [i,j]
        # return []
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res