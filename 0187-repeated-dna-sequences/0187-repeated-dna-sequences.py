class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq = defaultdict(int)
        for i in range(len(s) - 9):
            substring = s[i:i+10]
            freq[substring] += 1
        return [substring for substring in freq if freq[substring] > 1]