# 111000 -> 110001 -> 100011 -> 

# 111000 -> 101000 -> 101010


# 0(n)

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s+s
        len_t = len(t)
        pa = ''.join(['0' if i%2==0 else '1' for i in range(len_t)])
        pb = ''.join(['1' if i%2==0 else '0' for i in range(len_t)])
        mismatcha = 0
        mismatchb = 0
        answer = float('inf')
        for i in range(n):
            mismatcha += int(t[i])^int(pa[i])
            mismatchb += int(t[i])^int(pb[i])
        answer = min(mismatcha, mismatchb)

        print(f"answer: {answer}")

        left = 0
        for right in range(n, 2*n):
            mismatcha -= int(t[left])^int(pa[left])
            mismatcha += int(t[right])^int(pa[right])
            mismatchb -= int(t[left])^int(pb[left])
            mismatchb += int(t[right])^int(pb[right])
            left += 1
            answer = min(answer, min(mismatcha, mismatchb))

        return answer
s=Solution()
s.minFlips('111000')
        
            
# 110000 -> 
#   111100 -> 101100 -> 101000 -> 101010 (3)
#   111100 -> 011100 -> 010100 -> 010101 (3)
#   111100 -> 111001 ->
# 
# 111000 # len = 6 -> 101010 or 010101

# 111000
# 101010
# 010010 -> 2 flips

# 111000
# 010101
# 101101 -> 4 flips


########
# 001
# 010
# 011 -> 2 flips

# 001
# 101
# 100 -> 1 flip

# without flipping:
# 001 -> 010

# s  = "001"
# pa = "010010"
# pb = "101101"
# s XOR pa[:n] =
# s XOR pa[n:] =

# s = "001001" -> 010001 -> 
# 