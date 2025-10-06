class Solution:
    def reverseBits(self, n: int) -> int:
       ## .zfill(32) is used to ensure that the string is 32 bit
       s = bin(n)[2:].zfill(32)
       res = s[::-1]
       return int(res,2)