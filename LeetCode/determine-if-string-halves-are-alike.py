class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s_new = s.upper()
        a = s_new[:len(s)//2]
        b = s_new[len(s)//2:]

        vowels = ['A', 'E', 'I', 'O', 'U']
        a_count = 0
        b_count = 0
        
        for i in range(len(s)//2):
            if a[i] in vowels:
                a_count += 1
            if b[i] in vowels:
                b_count += 1
        if a_count == b_count:
            return True
        return False

        

s=Solution()
print(s.halvesAreAlike("book"))
print(s.halvesAreAlike("textbook"))