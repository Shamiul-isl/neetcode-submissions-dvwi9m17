class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        maxarea = 0
        while start < end:
            curarea = min(heights[start], heights[end]) * (end - start)
            maxarea = max(curarea, maxarea)
            if heights[start] < heights[end]:
                start+=1
            else:
                end-=1
        return maxarea