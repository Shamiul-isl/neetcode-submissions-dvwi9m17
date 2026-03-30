class Solution:
    def isPalindrome(self, s: str) -> bool:
        back, front = 0, len(s) - 1
        while back < front:
            while back < len(s) and s[back].isalnum() != True:
                back += 1
            while front > -1 and s[front].isalnum() != True:
                front -= 1
            if back < front and s[back].lower() != s[front].lower():
                return False
            back += 1
            front -= 1
        return True