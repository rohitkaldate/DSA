import sys
sys.set_int_max_str_digits(100000)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s="".join(map(str,num))
        op = int(s) + int(k)
        l = str(op)
        return list(map(int,l))