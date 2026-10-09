class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        maxDiff = 0
        i = 0
        for price in prices:
            if price < smallest:
                smallest = price
            maxDiff = max(maxDiff, (price-smallest))
            i+=1
        return maxDiff