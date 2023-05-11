from typename import typename


def test_typename_int():
    assert typename(5) == 'int'


def test_typename_float():
    assert typename(37.5) == 'float'
