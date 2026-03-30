class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            curSum = numbers[start] + numbers[end]
            if curSum > target:
                if numbers[start + 1] + numbers[end] > numbers[start] + numbers[end - 1]:
                    end -= 1
                else:
                    start += 1
            elif curSum < target:
                if numbers[start] + numbers[end - 1] < numbers[start + 1] + numbers[end]:
                    start += 1
                else:
                    end -= 1
            else:
                return [start + 1, end + 1]