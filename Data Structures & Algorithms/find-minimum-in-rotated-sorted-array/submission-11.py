"""
SCRATCH:
[8,9,0,1,2,3,4,5,6,7]
[3,4,5,6,1,2]
[4,5,0,1,2,3]
get the left val, right val, mid
if right val is less than left and mid, we're gonna move left to mid and recalculate mid, do the opposite for left less than right.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, (len(nums)-1)
        while r > (l+1):
            mid = l+(r-l)//2 #recalc mid each time
            if nums[r] < nums[mid]:
                l = mid
                continue
            elif nums[r] > nums[mid]:
                r = mid
                continue
        print(l,r)
        if nums[l] > nums[r]:
            return nums[r]
        else:
            return nums[l]