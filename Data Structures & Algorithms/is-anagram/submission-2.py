class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        for c in t:
            if c not in seen or seen[c] == 0:
                return False
            else:
                seen[c] -= 1

        return True