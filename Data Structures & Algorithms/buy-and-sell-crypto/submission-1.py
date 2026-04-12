class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic sized window
        # track the maxProfit 
        # init start and end of window to the start of the prices
        # while end pointer is not at the end of prices
            # iterate end pointer forwards 
            # profit =  prices[end] - prices[start]
            # if profit < maxProfit
                # iterate start pointer forwards

            # maxProfit = max(profit, maxProfit)

        # return maxProfit

        maxProfit = 0
        start, end = 0, 0

        while end < len(prices) - 1:
            end += 1

            # new minimum price found
            if prices[end] < prices[start]:
                start = end
                
            profit = prices[end] - prices[start]
            maxProfit = max(profit, maxProfit)

        return maxProfit