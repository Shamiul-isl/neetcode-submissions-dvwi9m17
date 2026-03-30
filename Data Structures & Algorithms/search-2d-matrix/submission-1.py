class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1
        while u <= d:
            mid = ((d - u) // 2) + u
            # print(mid)
            # print(matrix[mid][0])
            if matrix[mid][0] > target:
                d = mid - 1
            elif matrix[mid][0] < target:
                u = mid + 1
            else:
                return True
        # print(u)
        # print(d)
        row = None
        if u < len(matrix) and matrix[u][0] < target:
            row = u
        else:
            row = d
        print(row)
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = ((r - l) // 2) + l
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
