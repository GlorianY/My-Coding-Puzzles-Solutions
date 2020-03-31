def checkMagazine(magazine, note):
    magazine_words_count = Counter(magazine)

    for word in note:
        if word in magazine_words_count:
            if magazine_words_count[word] == 0:
                print('No')
                return False
            magazine_words_count[word] -= 1
        else:
            print('No')
            return False

    print('Yes')
    return True
