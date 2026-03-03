class Solution:

    def lastSubstring(self, s: str) -> str:
        
        mx = ""
        for i in range(len(s)):
            mx = max(mx, s[i:])
        print(mx)
        return mx
                
                
s = Solution()
s.lastSubstring(s = "abab")
s.lastSubstring(s = "leetcode")