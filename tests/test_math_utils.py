from my_project.math_utils import average, median, stddev

def test_average():
    assert average([1, 2, 3]) == 2
    assert average([5]) == 5
    assert average([]) is None

def test_median():
    assert median([1, 3, 2]) == 2
    assert median([4]) == 4
    assert median([]) is None

def test_stddev():
    assert round(stddev([1, 2, 3]), 5) == 1.0
    assert stddev([5]) is None
    assert stddev([]) is None