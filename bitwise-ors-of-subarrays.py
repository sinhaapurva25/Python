class Solution:
    def subarrayBitwiseORs(self, arr) -> int:
        # subarrs = list()
        st = set()
        for i in range(len(arr)):
            # tmp = list()
            res = 0
            for j in range(i, len(arr)):
                res |= arr[j]
                st.add(res)
                # tmp.append(arr[j])
                # subarrs.append(tmp[:])
        # print(subarrs)
        return len(st)
s = Solution()
# print(s.subarrayBitwiseORs(arr = [1,1,2]))
s.subarrayBitwiseORs(arr = [1,2,4])