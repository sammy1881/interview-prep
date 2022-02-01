class Solution:
    def containsDuplicate(nums):
        if not nums:
            return False
        else:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] == nums[j]:
                        return True


class betterSolution:
    def containsDuplicate(nums):
        if not nums:
            return False
        else:
            seen = {}
            for i in range(len(nums)):
                if nums[i] in seen:
                    return True
                else:
                    seen[nums[i]] = i
            return False
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums))
