class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        left  = 0
        res = 0
        for right in range(len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.add(s[right])
            res = max(right - left +1 ,res)
        return res
