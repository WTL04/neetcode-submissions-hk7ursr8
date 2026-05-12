class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        width = index
        height = value

        two pointer
        - one left pointer
        - one right pointer

        compare the values, and move the smallest value pointer
        store maximumAmount
        return maximumAmount
        """
        i, j = 0, len(heights) - 1
        maxArea = 0

        while i < j:
            area = (j - i) * min(heights[i], heights[j]) # width * height
            maxArea = max(area, maxArea)
            
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1


        return maxArea