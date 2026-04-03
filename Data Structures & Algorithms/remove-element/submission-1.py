class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        # iterate backwards
        # deletion from end of array is O(1) because there is
        # no need to shift the array
        for i in range(n-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)