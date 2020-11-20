from rhymes_with.rhymes import does_rhyme


def test_cook_rhymes_with_book():
    assert does_rhyme("book", "cook")


def test_fix_letter():
    assert not does_rhyme("book", "k")
    assert not does_rhyme("booc", "c")
    assert does_rhyme("a", "a")
