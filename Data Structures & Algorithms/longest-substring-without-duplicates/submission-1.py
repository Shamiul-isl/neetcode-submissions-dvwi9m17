class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0
        seen = set()

        while r < len(s):
            while l < r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            print(s[r])
            print(seen)
            seen.add(s[r])
            longest = max(longest, len(seen))
            r += 1
        
        return longest
