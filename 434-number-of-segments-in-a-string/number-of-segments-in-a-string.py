class Solution:
    def countSegments(self, s: str) -> int:
        #Returns the length of string by splitting it and converting in into the list
        l = s.split()
        return len(l)