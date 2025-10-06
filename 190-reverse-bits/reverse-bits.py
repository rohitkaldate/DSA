class Solution:
    def reverseBits(self, n: int) -> int:
       s = bin(n)[2:].zfill(32)
       res = s[::-1]
       return int(res,2)