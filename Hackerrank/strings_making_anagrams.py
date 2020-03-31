def makeAnagram(a, b):
    a_split = [x for x in a]
    b_split = [x for x in b]
    # get the unique letters from both inputs
    unique_letter = list(set(a_split + b_split))
    count = 0

    for letter in unique_letter:
        a_count = a.count(letter)
        b_count = b.count(letter)
        count += abs(a_count - b_count)
    return count
