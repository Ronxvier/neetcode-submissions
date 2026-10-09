class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        ct=0
        for num in nums:
            if target-num in mymap:
                return [mymap[target-num],ct]
            else:
                mymap[num] = ct
            ct+=1