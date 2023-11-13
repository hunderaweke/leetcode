class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = [i.lower() for i in s if i.isalpha() or i.isdigit()]
        return newS[::-1] == newS