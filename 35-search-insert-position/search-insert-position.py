class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
                break
            elif target < nums[i]+1:
                return i
        return len(nums)
                