class Solution:
    def reverse(self, x: int) -> int:
        ##reverse integer using the 32-bit integer range [-231, 231 - 1]
        if x<0:
            res = -int(str(-x)[::-1])
        else:
            res =  int(str(x)[::-1])
            
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res