def minimumSwaps(arr):
    swap_count = 0
    # algorithm : we only increase the counter when the currently traversed value (arr[i]) is already in the correct position
    i = 0
    while i < len(arr)-1:
        # if the value is not in the correct position,
        # then, put that value in the correct position
        # we know the correct position because the values are consecutive
        # this means, we know the correct position from the index
        if arr[i] != i+1:
            temp = arr[i]
            arr[temp - 1], arr[i] = arr[i], arr[temp - 1]
            swap_count += 1
        # increases the counter only if the currently traversed value (arr[i]) is already in the correct position
        else:
            i += 1
    return swap_count
