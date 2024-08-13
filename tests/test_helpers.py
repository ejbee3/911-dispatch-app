from helpers import get_test_length

def test_get_test_length():
    assert get_test_length('e') == 4
    assert get_test_length('m') == 7
    assert get_test_length('h') == 10


