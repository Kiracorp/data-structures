from data_structures import Stack
from .parameters import *
import pytest, random

def test_push():
    stack, arr = Stack(), []
    assert(stack.is_empty())
    for expected in range(ITERS):
        stack.push(expected)
        arr = [expected] + arr
        actual = stack.peek()
        assert(len(stack) == len(arr))
        assert(expected == actual)
        assert(not stack.is_empty())

def test_pop():
    stack, arr = Stack(), []
    assert(stack.is_empty())
    with pytest.raises(AssertionError):
        stack.pop()
    for _ in range(ITERS):
        expected = random.randrange(MAX_VAL)
        stack.push(expected)
        actual = stack.peek()
        arr = [expected] + arr
        assert(len(stack) == len(arr))
        assert(actual == expected)
    for _ in range(ITERS):
        expected, actual = arr[0], stack.pop()
        arr = arr[1:]
        assert(len(stack) == len(arr))
        assert(actual == expected)
    assert(stack.is_empty())
    with pytest.raises(AssertionError):
        stack.pop()