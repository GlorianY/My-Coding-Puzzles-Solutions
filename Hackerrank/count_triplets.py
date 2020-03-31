from collections import Counter

def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    for v in arr:
        if v in r3:
           # get the count from the r2, and increment r2 using that count
           # use the count from r3 (r3 stores the last value of a complete triplet)
           # so, if our v is 1,5,5,25, then we can get the count from both 5
           # as in 1,5 (from the first 5),25 and 1,5 (from the second 5),25
           count += r3[v]

        if v in r2:
           # increment the count of the "waiting" last r (triplet)
           # use the count from r2 (r2 stores the second value of a complete triplet)
           # e.g. if the v is 5 (in which we found in r2 where the value comes from the previous values 1 * 5) and r is 5, then the next value that we should find is 25 (from 5*5)
           r3[v*r] += r2[v]

        # increment the count of the "waiting" r
        # e.g. if the v is 1 and r is 5, then the r2 will be 5
        r2[v*r] += 1
    return count
