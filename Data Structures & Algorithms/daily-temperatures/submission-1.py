class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temp, i))
        for s in stack:
            res[s[1]] = 0
        return res

            
