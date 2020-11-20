import argparse
import sys

from rhymes_with import __version__
from rhymes_with.dictionary import read_dictionary_file
from rhymes_with.rhymes import filter_rhymes


def make_parser(program_name="rhymes_with"):
    """
    :param program_name: The name of the executable called.
    :returns: The parser of command-line arguments for the rhymes_with
        executable.
    """
    parser = argparse.ArgumentParser(
        prog=program_name,
        description="Gives a list of words that rhymes with the given word.",
    )
    parser.add_argument(
        "word",
        type=str,
        help="The word to find rhymes of",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    return parser


def parse_args(argv):
    """
    :param argv: The argument list, e.g. ["rhymes_with", "--version"].
    :returns: A argparse.namespace with the values
        parsed from the list of arguments.
    """
    parser = make_parser(argv[0])
    return parser.parse_args(argv[1:])


def run_rhymes_with(argv):
    """
    :param argv: The argument list, e.g. ["rhymes_with", "--version"].
    Runs rhymes_with on the given list of arguments.
    """
    args = parse_args(argv)
    dictionary = read_dictionary_file()
    rhyming_words = filter_rhymes(args.word, dictionary)
    for rhyme in rhyming_words:
        print(rhyme)


def main():
    run_rhymes_with(sys.argv)


if __name__ == "__main__":
    main()
