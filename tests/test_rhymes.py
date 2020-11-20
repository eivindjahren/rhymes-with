from rhymes_with.rhymes import does_rhyme


def test_cook_rhymes_with_book():
    assert does_rhyme("book", "cook")


def test_tick_pararhymes_with_tock():
    assert does_rhyme("tick", "tock")


def test_ticks_does_not_pararhymes_with_tock():
    assert not does_rhyme("ticks", "tock")
