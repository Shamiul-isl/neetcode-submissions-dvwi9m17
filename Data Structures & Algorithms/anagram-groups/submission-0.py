class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = {}
        for i in range(len(strs)):
            changed = False
            for key in seen.keys():
                if self.isAnagram(key, strs[i]):
                    seen[key].append(strs[i])
                    changed = True
                    break
            if not changed:
                seen[strs[i]] = []
        
        for key in seen.keys():
            seen[key].append(key)
            result.append(seen[key])
        return result

        
    def isAnagram(self, s: List[str], t: List[str]):
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