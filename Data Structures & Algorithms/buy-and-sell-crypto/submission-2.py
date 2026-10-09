class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        maxDiff = 0
        for price in prices:
            if price < smallest:
                smallest = price
            maxDiff = max(maxDiff, (price-smallest))
        return maxDiff