def sort_by_awesome(words: [str]) -> [str]:
    if "sloths" in words:
        words.remove("sloths")
        words.insert(0, "sloths")
    return words


def sort_word_by(words: [str], criteria) -> [str]:
    """
    :returns: The sorted list given by the criteria
    """
    if criteria == "alphabetically":
        return sorted(words)
    if criteria == "length":
        return sorted(words, key=len)
    if criteria == "awesome":
        return sort_by_awesome(words)
    else:
        raise NotImplementedError(
            f"The sorting criteria: {criteria} has not been implemented"
        )
