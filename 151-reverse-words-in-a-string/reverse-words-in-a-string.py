class Solution:
    def reverseWords(self, s: str) -> str:
        op = s.split()
        res = op[::-1]
        final_res = " ".join(map(str,res))
        return final_res