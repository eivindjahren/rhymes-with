from pathlib import Path

DICTIONARY_PATH = Path("/usr") / "share" / "dict" / "words"


def read_dictionary_file() -> [str]:
    dictionary = []
    with DICTIONARY_PATH.open("r") as dictionary_file:
        dictionary = dictionary_file.read().splitlines()
    return dictionary
