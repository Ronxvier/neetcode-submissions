class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for num in nums:
            if num in freqmap:
                freqmap[num] +=1
            else:
                freqmap[num] = 1
        answ = []
        list = sorted(freqmap.items(), key=lambda x: x[1])
        for i in range(0,k):
            answ.append(list.pop(-1)[0])
        return answ