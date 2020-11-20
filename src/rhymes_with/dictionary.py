from pathlib import Path

DICTIONARY_PATH = Path("/usr") / "share" / "dict" / "words"


def read_dictionary_file() -> [str]:
    """
    Reads the list of words in the file given
    by DICTIONARY_PATH
    """
    dictionary = []
    with DICTIONARY_PATH.open("r") as dictionary_file:
        dictionary = dictionary_file.read().splitlines()
    return dictionary
