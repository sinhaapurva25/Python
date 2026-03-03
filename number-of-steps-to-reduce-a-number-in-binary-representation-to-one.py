class Solution:
    def numSteps(self, s: str) -> int:
        dec = 0
        for i in range(len(s)):
            dec += int(s[i]) * (2 ** (len(s)-i-1))
        
        res=0
        while dec != 1:
            if dec%2 == 1:
                dec += 1
            else:
                dec = dec//2
            res += 1
        return res



        