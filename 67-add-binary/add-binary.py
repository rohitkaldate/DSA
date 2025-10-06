class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1=int(a,2)
        n2=int(b,2)
        n=bin(n1+n2)
        return n[2:]