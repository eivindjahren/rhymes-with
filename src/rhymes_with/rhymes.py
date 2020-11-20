import pronouncing


def does_rhyme(word1: str, word2: str) -> bool:
    """
    :returns: True if word1 and word2 rhymes
    """
    return word1 in pronouncing.rhymes(word2)


def filter_rhymes(word: str, dictionary: [str]) -> [str]:
    """
    :returns: the strings in dictionary that does_rhyme
        with word.
    """
    return filter(lambda w: does_rhyme(word, w) and w != word, dictionary)
