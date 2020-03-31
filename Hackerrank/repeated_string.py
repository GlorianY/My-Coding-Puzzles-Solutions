def repeatedString(s, n):

    count_original = s.count('a')

    remainder = n // len(s)

    count_long_s = count_original * remainder
    remainder_from_n = n - (len(s) * remainder)
    result = count_long_s + s[:remainder_from_n].count('a')

    return result
