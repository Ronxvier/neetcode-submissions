class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        currmax = 0
        while r>l:
            vol = min(heights[r],heights[l]) * (r-l)
            if vol > currmax:
                currmax = vol
            if heights[r]>heights[l]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                vol = min(heights[r],heights[l]) * (r-l)
                if vol > currmax:
                    currmax = vol
                l+=1
        return currmax