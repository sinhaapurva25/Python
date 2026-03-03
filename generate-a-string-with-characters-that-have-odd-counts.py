class Solution:
    def generateTheString(self, n: int) -> str:

        if n %2 == 0:
            res = ['a']
            res.extend(['b' for _ in range(n-1)])
        else:
            if n == 1:
                return 'a'
            res = ['a']
            res.append('b')
            res.extend(['c' for _ in range(n-2)])
        return "".join(res)
s = Solution()
print(s.generateTheString(4))
print(s.generateTheString(2))
print(s.generateTheString(7))