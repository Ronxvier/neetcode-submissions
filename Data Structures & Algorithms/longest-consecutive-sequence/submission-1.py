class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        currct = 1
        maxct=0
        for num in nums:
            if num-1 not in nums:
                while num+1 in nums:
                    currct+=1
                    num = num+1
                maxct = max(maxct,currct)
            currct = 1
        return maxct