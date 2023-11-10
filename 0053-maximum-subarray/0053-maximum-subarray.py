class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        runSum = 0
        for right in range(len(nums)):
            if runSum <0:
                runSum = 0
            runSum += nums[right]
            res = max(res,runSum)
        return res