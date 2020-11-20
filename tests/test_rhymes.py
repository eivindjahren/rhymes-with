from rhymes_with.rhymes import does_rhyme


def test_cook_rhymes_with_book():
    assert does_rhyme("book", "cook")


def test_rhyme_rhymes_with_sublime():
    assert does_rhyme("rhyme", "sublime")


def test_cook_rhymes_with_family():
    assert not does_rhyme("book", "family")
