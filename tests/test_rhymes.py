from rhymes_with.rhymes import does_rhyme


def test_cook_rhymes_with_book():
    assert does_rhyme("book", "cook")


def test_weary_rhymes_with_veterinary():
    assert does_rhyme("weary", "veterinary")
