class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        solution = []
        zindex = 0
        i=0
        zct=0
        for num in nums:
            if num == 0:
                zindex=i
                zct+=1
            else:
                product *=num
            i+=1
        if zct > 1:
            return [0] * len(nums)
        elif zct == 1:
            solution = [0] * len(nums)
            solution[zindex] = product
            return solution
        else:
            for num in nums:
                if num == 0:
                    solution.append(int(product))
                else:
                    solution.append(int(product/num))
            return solution