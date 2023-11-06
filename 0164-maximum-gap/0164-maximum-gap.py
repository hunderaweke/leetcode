class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:return 0
        res = float('-inf')
        nums.sort()
        left = 0
        for right in range(1,len(nums)):
            diff = nums[right] - nums[left]
            left += 1
            res = max(diff,res)
        return res