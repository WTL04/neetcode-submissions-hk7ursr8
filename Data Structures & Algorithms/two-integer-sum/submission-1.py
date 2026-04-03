class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            diff = target - n # calculate complement
            if diff in prev:  # if complement in prev, return index of complement and current index
                return [prev[diff], i]
            prev[n] = i # store index