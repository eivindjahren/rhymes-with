def does_rhyme(word1: str, word2: str, length: int = 3) -> bool:
    """
    :returns: True iff word1 and word2 has the
        same ending up to length.
    """
    length = min(3, len(word1), len(word2))

    if word1[-length:] == word2[-length:]:
        return True
    else:
        if word1[-length:] == "yme" and word2[-length:] == "ime":
            return True
        if word2[-length:] == "yme" and word1[-length:] == "ime":
            return True

    return False


def filter_rhymes(word: str, dictionary: [str]) -> [str]:
    """
    :returns: the strings in dictionary that does_rhyme
        with word.
    """
    return filter(lambda w: does_rhyme(word, w) and w != word, dictionary)
