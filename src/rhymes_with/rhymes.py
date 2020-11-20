def does_rhyme(word1: str, word2: str, length: int = 3) -> bool:
    """
    :returns: True if word1 and word2 rhymes.
    """
    return does_perfectly_rhyme(word1, word2)


def does_perfectly_rhyme(word1: str, word2: str, length: int = 3) -> bool:
    """
    :returns: True iff word1 and word2 has the
        same ending up to length.
    """
    length = min(3, len(word1), len(word2))
    return word1[-length:] == word2[-length:]


def filter_rhymes(word: str, dictionary: [str]) -> [str]:
    """
    :returns: the strings in dictionary that does_rhyme
        with word.
    """
    return filter(lambda w: does_rhyme(word, w) and w != word, dictionary)
