class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        solution=[intervals[0]] # first interval
        for i in range(1,len(intervals)):
            prev = solution[-1]
            curr = intervals[i]
            # case one: consumed
            if curr[0] < prev[0] and curr[1] > prev[1]:
                solution[-1] == curr
            # case two: joint
            elif curr[0] <= prev[1] and curr[1] >= prev[1]:
                solution[-1] = [prev[0],curr[1]]
            # case three: disjoint
            elif curr[0] > prev[1]:
                solution.append(curr)
        return solution

