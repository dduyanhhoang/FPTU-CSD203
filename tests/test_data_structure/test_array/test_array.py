import pytest
from data_structure.array.array import Array

def test_initialization():
    arr = Array(10)
    assert len(arr) == 10
    assert arr.capacity == 10