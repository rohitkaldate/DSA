class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            l.append(nums[i]*nums[i])
        
        l.sort()
        return l

        # return nums
        