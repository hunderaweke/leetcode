class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        hashmap = Counter()
        curSum = 0
        for num in nums:
            curSum += num
            if curSum % k == 0:
                res += 1
            res += hashmap[curSum%k]
            hashmap[curSum % k] += 1
        return res