def twoSum(nums, target):
    hashmap = {}
    for i, v in enumerate(nums):
        remaining = target - v

        if remaining in hashmap:
            return[hashmap[remaining], i]

        hashmap[v] = i
