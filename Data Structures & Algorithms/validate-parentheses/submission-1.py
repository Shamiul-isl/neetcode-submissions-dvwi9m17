class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for c in s:
            if c == '}' or c == ']' or c == ')':
                if len(seen) == 0:
                    return False
                cur = seen.pop()
                if (c == '}' and cur != '{') or (c == ']' and cur != '[') or (c == ')' and cur != '('):
                    return False
            else:
                seen.append(c)
        return len(seen) == 0