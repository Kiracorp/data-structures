from data_structures import LinkedList
import pytest, random

ITERS = 100

@pytest.fixture
def base_ll():
    ll = LinkedList()
    for i in range(ITERS):
        ll.insert_tail(i)
    return ll

def test_repr():
    ll = LinkedList()
    for i in range(5):
        ll.insert_tail(i)
    assert(repr(ll) == "0 {data: 0} -> 1 {data: 1} -> "\
        "2 {data: 2} -> 3 {data: 3} -> 4 {data: 4}")

def test_ll_equality():
    ll1, ll2 = LinkedList(), LinkedList()
    for i in range(ITERS): 
        ll1.insert_head(i)
        ll2.insert_head(i)
    assert(ll1 == ll2)

def test_index_of(base_ll):
    ll = base_ll
    for i in range(len(ll)):
        actual = ll.index_of(i)
        expected = i
        assert(actual == expected)
    assert(ll.index_of(-1) == -1)
    assert(ll.index_of(len(ll)) == -1)

def test_insert_invalid():
    ll = LinkedList()
    for i in range(-ITERS//2, 0):
        with pytest.raises(AssertionError):
            ll.insert(i, 0)
    for i in range(1, ITERS//2+1):
        with pytest.raises(AssertionError):
            ll.insert(i, 0)
    assert(ll.is_empty())

def test_pop_invalid():
    ll = LinkedList()
    with pytest.raises(AssertionError):
        ll.pop(0)
    ll.insert(0, 0)
    for i in range(-ITERS//2, ITERS//2+1):
        if i == 0: continue
        with pytest.raises(AssertionError):
            ll.pop(i)

def test_peek_invalid():
    ll = LinkedList()
    with pytest.raises(AssertionError):
        ll.peek(0)
    ll.insert(0, 0)
    for i in range(-ITERS//2, ITERS//2+1):
        if i == 0: continue
        with pytest.raises(AssertionError):
            ll.peek(i)

def test_insert_head():
    ll = LinkedList()
    for i in range(ITERS):
        ll.insert_head(i)
        assert(len(ll) == i+1)
        assert(ll.peek_head() == i)

def test_insert_tail():
    ll = LinkedList()
    for i in range(ITERS):
        ll.insert_tail(i)
        assert(len(ll) == i+1)
        assert(ll.peek_tail() == i)

def test_pop_head(base_ll):
    ll = base_ll
    for expected in range(len(ll)):
        actual = ll.pop_head()
        assert(expected == actual)
    assert(ll.is_empty())

def test_pop_tail(base_ll):
    ll = base_ll
    for expected in range(len(ll)-1, -1, -1):
        actual = ll.pop_tail()
        assert(actual == expected)
    assert(ll.is_empty())

def test_pop_only_element():
    ll = LinkedList()
    for data in [0, "a", 1.5, [], {}, LinkedList()]:
        ll.insert(0, data)
        assert(not ll.is_empty())
        assert(id(ll.peek_head()) == id(ll.peek_tail()))
        actual = ll.pop(0)
        assert(ll.is_empty())
        assert(actual == data)

def test_random_ops():
    ll, arr = LinkedList(), []
    for i in range(ITERS):
        index = random.randrange(i+1)
        data = random.randrange(5000)
        ll.insert(index, data)
        arr.insert(index, data)
        assert(ll.to_array() == arr)
    for i in range(ITERS):
        index = random.randrange(ITERS)
        actual = ll.peek(index)
        expected = arr[index]
        assert(actual == expected)
    for i in range(ITERS, 0, -1):
        index = random.randrange(i)
        actual = arr.pop(index)
        expected = ll.pop(index)
        assert(actual == expected)
        assert(ll.to_array() == arr)
    assert(ll.is_empty() and len(arr) == 0)