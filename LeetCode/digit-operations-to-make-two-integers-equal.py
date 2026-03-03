class Solution:
    def minOperations(self, n: int, m: int) -> int:

        def isPrime(num: int):
            if num > 1:            
                if num == 2:
                    return True
                c = 0
                for i in range(1, num+1):
                    if num%i == 0:
                        c += 1
                    if c > 2:
                        return False
                if c == 2:
                    return True
            return False
        
        while not isPrime(n):
            
            pass
        return -1
s = Solution()
for i in range(1, 100):
    if s.minOperations(i,i): print(f"{i} is a prime number")