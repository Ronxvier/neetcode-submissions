"""
nums = [-1,0,1,2,-1,-4]
nums.sorted() -> [-4,-1,-1,0,1,2]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for i in range(len(nums)-2):
            r = len(nums)-1
            l = i+1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while r>l:
                triplet = [nums[i],nums[l],nums[r]]
                s = sum(triplet)
                if s == 0:
                    solution.append(triplet)
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif s > 0:
                    r-=1
                elif s<0:
                    l+=1
        return solution
