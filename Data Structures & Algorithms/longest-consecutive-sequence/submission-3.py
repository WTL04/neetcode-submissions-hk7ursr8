class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        # sort and remove duplicates
        nums = sorted(nums)

        maxCount = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
                
            if nums[i-1] == nums[i] - 1:
                count += 1
            else:
                # reset count when sequence breaks
                maxCount = max(count, maxCount)
                count = 1
        
        # Final check to capture the last sequence
        maxCount = max(count, maxCount)

        return maxCount
