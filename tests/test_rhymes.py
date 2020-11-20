import pytest

from rhymes_with.rhymes import does_rhyme


def test_cook_rhymes_with_book():
    assert does_rhyme("book", "cook")


def test_cough_not_rhymes_with_bough():
    assert not does_rhyme("cough", "bough")


@pytest.mark.parametrize(
    "word_1, word_2",
    [["rhyme", "sublime"], ["picky", "tricky"]],
)
def test_perfect_rhyme(word_1, word_2):
    assert does_rhyme(word_1, word_2)
