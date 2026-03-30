class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key in seen.keys():
            buckets[seen[key]].append(key)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    return result
        
        return result