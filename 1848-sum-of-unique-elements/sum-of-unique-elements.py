class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # l=list(set(nums))
        # return l
        total = 0
        for num in nums:
            if nums.count(num)==1:
                total += num
        return total
        return 0