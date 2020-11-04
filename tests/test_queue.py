from data_structures import Queue
from .parameters import *
import pytest, random

def test_push():
    queue = Queue()
    assert(queue.is_empty())
    for i in range(ITERS):
        queue.push(i)
        assert(len(queue) == i+1)
        assert(queue.peek() == 0)
        assert(not queue.is_empty())

def test_pop():
    queue, arr = Queue(), []
    assert(queue.is_empty())
    with pytest.raises(AssertionError):
        queue.pop()
    for _ in range(ITERS):
        value = random.randrange(MAX_VAL)
        queue.push(value)
        arr.append(value)
        assert(len(queue) == len(arr))
    for _ in range(ITERS):
        assert(not queue.is_empty())
        expected, arr = arr[0], arr[1:]
        actual = queue.peek()
        assert(actual == expected)
        actual = queue.pop()
        assert(actual == expected)
        assert(len(queue) == len(arr))
    assert(queue.is_empty())
    with pytest.raises(AssertionError):
        queue.pop()