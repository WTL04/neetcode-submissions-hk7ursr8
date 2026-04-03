class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a hash to track freq
        # if int in nums already in hash, return false, else return true

        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                return True

        return False
            