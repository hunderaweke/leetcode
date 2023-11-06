class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):return []
        pCounter,winCounter = {},{}
        for i  in range(len(p)):
            pCounter[p[i]] = 1+pCounter.get(p[i],0)
            winCounter[s[i]] = 1+winCounter.get(s[i],0)
        res  = [0] if pCounter == winCounter else []
        left = 0
        for i in range(len(p),len(s)):
            winCounter[s[i]] = 1 + winCounter.get(s[i],0)
            winCounter[s[left]] -= 1
            if winCounter[s[left]] ==0:
                winCounter.pop(s[left])
            left+=1
            if pCounter == winCounter:
                res.append(left)
        return res