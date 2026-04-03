class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        result[i] = prefix[i] * postfix[i]
        - prefix computes the product up to (but NOT including) index i
        - postfix computes the product after (but NOT including) index i
        """
        n = len(nums)

        prefix = [0] * n
        postfix = [0] * n
        output = [0] * n

        prefix[0] = 1       # nothing to the left of index 0
        postfix[n - 1] = 1  # nothing to the right of last index

        # build prefix array
        for i in range(1, n):

            # start from index 1
            # start calculation from prefix[0] * nums[0]
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(n - 2, -1, -1):

            # start from index n - 2
            # start calculation from prefix[n - 1] * nums[n - 1]
            postfix[i] = nums[i + 1] * postfix[i + 1]

        for i in range(n):
            output[i] = prefix[i] * postfix[i]

        return output
