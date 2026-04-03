class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        maxLength = 0
        n = len(nums)

        count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count = 0

            maxLength = max(maxLength, count)

        return maxLength

            

