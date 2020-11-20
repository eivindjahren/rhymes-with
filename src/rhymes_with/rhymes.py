def does_rhyme(word1: str, word2: str, verbosity, length: int = 3) -> bool:
    """
    :returns: True iff word1 and word2 has the
        same ending up to length.
    """
    length = min(3, len(word1), len(word2))
    result = word1[-length:] == word2[-length:]
    if verbosity:
        print("Verbosity is on")
        print(f"Checking if the word {word1} rhymes with {word2}: {result}")
    return result


def filter_rhymes(word: str, dictionary: [str], verbosity) -> [str]:
    """
    :returns: the strings in dictionary that does_rhyme
        with word.
    """

    return filter(lambda w: does_rhyme(word, w, verbosity) and w != word, dictionary)
