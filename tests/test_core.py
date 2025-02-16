
import pytest
from learning_pypi.core import sum_numbers

def test_sum_numbers():
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers([1, 2, 3, 4, 5]) == 15 
    assert sum_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert sum_numbers([]) == 0
    assert sum_numbers([-1, -2, -3]) == -6
    assert sum_numbers([5]) == 5