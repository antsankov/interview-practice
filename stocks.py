# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Input: 
#Output: 5

# Input: [7,6,4,3,1]
# Output: 0

def maxProfit(prices):
    profit = 0
    for x in range(0, len(prices)):
        for y in range(x, len(prices)):
            if (prices[y] > prices[x]):
                trade = prices[y] - prices[x]
                if (trade > profit):
                    profit = trade
                    print("try " + str(trade))
                    print(str(prices[x]) + " " + str(prices[y]))
    
    print("FINAL " + str(profit))


maxProfit([7,1,5,3,6,4])
maxProfit([7,6,4,3,1])