def maximumToys(prices, k):
    # make sure the prices are sorted
    prices.sort()
    i = 0
    while k > 0 :
        k -= prices[i]
        i += 1
    return i – 1
