class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurse(step):
            if step==n:
                return 1
            elif step>n:
                return 0
            if step in memo:
                return memo[step]
            res = recurse(step+1) + recurse(step+2)
            memo[step] = res
            return res
        return recurse(0)
            