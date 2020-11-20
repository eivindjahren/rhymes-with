from rhymes_with.sorter import sort_word_by

def test_alphabetically():
    assert sort_word_by(["tree", "clown", "super"], "alphabetically") == ['clown', 'super', 'tree']

def test_awesome():
    assert sort_word_by(["owls", "sloths", "red-pandas"], "awesome") == ["sloths", "owls", "red-pandas"]
