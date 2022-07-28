def maxProfit(prices): #Sliding window problem
    sum = 0
    lowest = 0
    for i in range(len(prices)):
        if prices[i] < prices[lowest]:
            lowest = i
        sum = max(sum, prices[i] - prices[lowest])
    return sum

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
