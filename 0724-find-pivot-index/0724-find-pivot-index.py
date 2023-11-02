class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = float('inf')
        preSum = [0]*len(nums)
        preSum[0] += nums[0]
        for i in range(1,len(nums)):
            preSum[i] = nums[i] + preSum[i-1]
        for p in range(len(nums)):
            if p == 0: 
                if (preSum[-1] - preSum[p] == 0):
                    res = min(res , p)
            elif preSum[-1] - preSum[p] == preSum[p-1]:
                res =  min(res , p)
        return res if res != float('inf') else -1