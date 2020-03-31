def twoStrings(s1, s2):
    #algorithm : break the word into letters, and find the intersection between letters in two lists
    if len(list(set(list(s1)) & set(list(s2)))) > 0:
        return "YES"
    else:
        return "NO"
