class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ##Difference between two strings
        s_count, t_count = Counter(s), Counter(t)
        for ch in t_count:
            if t_count[ch] != s_count.get(ch, 0):
                return ch
