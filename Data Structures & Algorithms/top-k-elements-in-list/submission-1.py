import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        # first = 0
        # second = 0

        # for key in seen.keys():
        #     if first == 0:
        #         first = key
        #         second = key
        #         continue
        h = []
        for key in seen.keys():
            heapq.heappush_max(h, (seen[key], key))
        # print(h)
        # heapq.heappop(h)
        # print(h)
        # heapq.heapify_max(h)
        # print(h)
        result = []
        for i in range(k):
            result.append(heapq.heappop(h)[1])
            heapq.heapify_max(h)
        return result
            