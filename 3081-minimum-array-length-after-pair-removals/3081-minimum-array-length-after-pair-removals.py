class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        left = 0
        right  = (len(nums)+1)//2
        pairs = 0
        while left < len(nums)//2 and right < len(nums):
            if nums[left] < nums[right]:
                pairs += 2
            left += 1
            right += 1
        return len(nums) - pairs