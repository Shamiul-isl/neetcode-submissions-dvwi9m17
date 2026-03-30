class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, lastmax, maximum = prices[0], prices[0], 0
        for v in prices:
            if v < minimum:
                maximum = max(lastmax - minimum, maximum) if maximum != 0 else lastmax - minimum
                minimum = v
                lastmax = v
            elif v > lastmax:
                lastmax = v

        return max(lastmax - minimum, maximum) if maximum != 0 else lastmax - minimum
