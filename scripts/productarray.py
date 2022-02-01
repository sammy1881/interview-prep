import numpy


class Solution:
    def productExceptSelf(nums):
        result = []
        for i in range(len(nums)):
            out = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    out = out * nums[j]
            result.append(out)
        return(result)

    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
