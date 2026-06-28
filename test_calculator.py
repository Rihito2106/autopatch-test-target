from calculator import divide, average, find_max


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    # Bug: this raises ZeroDivisionError instead of returning None
    result = divide(10, 0)
    assert result is None


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0


def test_average_empty():
    # Bug: this raises ZeroDivisionError instead of returning 0
    result = average([])
    assert result == 0


def test_find_max():
    assert find_max([3, 1, 4, 1, 5, 9]) == 9
