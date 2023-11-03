class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashMap = {0:0}
        curSum = 0
        for index in range(len(nums)):
            curSum += nums[index]
            if curSum % k not in hashMap:
                hashMap[curSum%k] = index +1
            if hashMap[curSum % k] < index:
                return True
        return False