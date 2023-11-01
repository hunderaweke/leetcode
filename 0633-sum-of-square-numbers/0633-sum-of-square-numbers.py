class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5)+1):
            new_b = (c-(a*a))**0.5
            if new_b == int(new_b):
                return True
        return False