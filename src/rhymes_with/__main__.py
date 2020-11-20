import argparse
import sys

from rhymes_with import __version__
from rhymes_with.dictionary import read_dictionary_file
from rhymes_with.rhymes import filter_rhymes


def make_parser(prog):
    parser = argparse.ArgumentParser(
        prog=prog, description="Gives a list of words that rhymes with the given word."
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
    parser = make_parser(argv[0])
    return parser.parse_args(argv[1:])


def run_rhymes_with(args):
    args = parse_args(sys.argv)
    dictionary = read_dictionary_file()
    rhyming_words = filter_rhymes(args.word, dictionary)
    for rhyme in rhyming_words:
        print(rhyme)


def main():
    run_rhymes_with(sys.argv)


if __name__ == "__main__":
    main()
