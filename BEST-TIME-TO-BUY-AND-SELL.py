#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

           
        min_price = float('inf')  # Start with a very high value for the minimum price
        max_profit = 0  # Start with 0 as we might not make any profit

        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price when we find a lower price
            profit = price - min_price  # Calculate the profit if sold today
            if profit > max_profit:
                max_profit = profit  # Update max_profit if we found a better profit

        return max_profit

        