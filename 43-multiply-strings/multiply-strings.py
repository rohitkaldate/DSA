import sys
sys.set_int_max_str_digits(10000)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = int(num1) * int(num2)
        return str(res)