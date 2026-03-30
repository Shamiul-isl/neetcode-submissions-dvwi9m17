class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        l = 0
        for c in s1:
            seen[c] = 1 + seen.get(c, 0)
        temp = dict(seen)
        for r in range(len(s2)):
            if s2[r] in temp:
                while temp[s2[r]] == 0 and l <= r:
                    temp[s2[l]] += 1
                    l += 1
                temp[s2[r]] -= 1
                if r - l + 1 == len(s1):
                    return True
            else:
                l = r + 1
                temp = dict(seen)
        
        for key in temp.keys():
            if temp[key] > 0:
                return False
        
        return True

