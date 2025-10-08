class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp = num
        rev1 = 0
        rev2 = 0

        while num>0:
            digit = num%10
            rev1 = rev1*10+digit
            num = num//10
    
        while rev1>0:
            d = rev1%10
            rev2 = rev2*10+d
            rev1 = rev1//10

        if rev2 == temp:
            return True
        else:
            return False
