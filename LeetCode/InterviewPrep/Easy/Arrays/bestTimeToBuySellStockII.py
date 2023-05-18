class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        current_buy = None
        total_profit = 0
        for index, current_price in enumerate(prices):
            if type(current_buy) == int:
                if current_buy < current_price:
                    total_profit += current_price - current_buy
                    current_buy = None
            if index + 1 < len(prices):
                #Index is in range of prices
                if prices[index + 1] > current_price:
                    current_buy = current_price
        return total_profit