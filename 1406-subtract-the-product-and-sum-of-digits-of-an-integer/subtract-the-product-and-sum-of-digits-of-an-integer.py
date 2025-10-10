class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = sum(int(digit) for digit in str(n))
        product = 1
        while n!=0:
            product = product*(n%10)
            n=n//10
        return product - s
        # return s