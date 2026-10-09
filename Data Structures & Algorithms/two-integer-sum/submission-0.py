class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        i=0
        for num in nums:
            if (target-num) in map:
                return [map.get(target-num), i]
            else:
                map.update({num: i})
                i+=1