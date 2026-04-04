class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n):

            # skip over duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    # three sum found, iterate pointers
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1

                    # move left forwards until no duplicates
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
