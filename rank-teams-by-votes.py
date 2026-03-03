class Solution:

    def rankTeams(self, votes) -> str:
        n = len(votes[0])
        dct = {c: [0]*n for c in votes[0]}
        print(dct)
        
        for vote in votes:
            for i, team in enumerate(vote):
                dct[team][i] += 1
        print(dct)
        
        # return "".join(k for k, _ in sorted(dct.items(),key=lambda x: (-x[1], x[0])))
        return "".join(k for k, _ in sorted(dct.items(),key=lambda x: ([-c for c in x[1]], x[0])))
s = Solution()
print(s.rankTeams(votes = ["WXYZ","XYZW"]))
# print(s.rankTeams(votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))