
def sort_word_by(words: [str], criteria) -> [str]:
    """
    :returns: The sorted list given by the criteria
    """
    if criteria == "alphabetically":
        return sorted(words)
    else:
        raise NotImplementedError(f"The sorting criteria: {criteria} has not been implemented")
