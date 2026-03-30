class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 0
        ret = []
        includes_zero = False
        includes_zero_twice = False
        for num in nums:
            if num == 0:
                if not includes_zero_twice and includes_zero:
                    includes_zero_twice = True
                else:
                    includes_zero = True
                continue
            if res == 0 and num != 0:
                res = num
                continue
            res *= num
        if includes_zero_twice:
            res = 0
        for num in nums:
            if num == 0:
                ret.append(res)
            elif includes_zero:
                ret.append(0)
            else:
                ret.append(res//num)
        return ret
