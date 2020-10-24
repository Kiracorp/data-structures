from data_structures import LinkedList
import pytest

@pytest.fixture
def empty_ll_setup():
    return LinkedList(), 10

@pytest.fixture
def base_ll():
    ll = LinkedList()
    for data in range(6):
        ll.insert_tail(data)
    return ll

def test_repr(base_ll):
    assert(repr(base_ll) == "0 {data: 0} -> 1 {data: 1} -> "\
        "2 {data: 2} -> 3 {data: 3} -> 4 {data: 4} -> 5 {data: 5}")

def test_insert_invalid(empty_ll_setup):
    ll, iters = empty_ll_setup
    assert(ll.is_empty())
    assert(ll.index_of(0) == -1)
    for i in range(-iters//2, 0):
        with pytest.raises(AssertionError):
            ll.insert(i, 0)
    for i in range(1, iters//2+1):
        with pytest.raises(AssertionError):
            ll.insert(i, 0)

def test_insert_head(empty_ll_setup):
    ll, iters = empty_ll_setup
    for i in range(iters):
        ll.insert_head(i)
        assert(len(ll) == i+1)
        assert(ll.peek_head() == i)

def test_insert_tail(empty_ll_setup):
    ll, iters = empty_ll_setup
    for i in range(iters):
        ll.insert_tail(i)
        assert(len(ll) == i+1)
        assert(ll.peek_tail() == i)

def test_insert_inner(base_ll):
    orig_size = start_val = len(base_ll)
    def inner_insertion(index, val):
        base_ll.insert(index, val)
        assert(len(base_ll) == val+1)
        assert(base_ll.index_of(val) == index)
    inner_insertion(1, start_val)
    inner_insertion(orig_size, start_val+1)
    inner_insertion(orig_size//2, start_val+2)

def test_remove_invalid(empty_ll_setup):
    ll, iters = empty_ll_setup
    for i in range(-iters//2, iters//2+1):
        with pytest.raises(AssertionError):
            ll.remove(i)

def test_remove_only_element():
    ll = LinkedList()
    for data in [0, "a", 1.5, [], {}, LinkedList()]:
        ll.insert(0, data)
        assert(not ll.is_empty())
        assert(id(ll.peek_head()) == id(ll.peek_tail()))
        actual = ll.remove(ll.index_of(data))
        assert(ll.is_empty())
        assert(actual == data)

def test_remove_head(base_ll):
    for expected in range(len(base_ll)):
        actual = base_ll.remove_head()
        assert(expected == actual)
    assert(base_ll.is_empty())

def test_remove_tail(base_ll):
    for expected in range(len(base_ll)-1, -1, -1):
        actual = base_ll.remove_tail()
        assert(actual == expected)
    assert(base_ll.is_empty())

def test_remove_inner(base_ll):
    orig_data = base_ll.peek_all()
    orig_size = len(base_ll)
    expected = len(base_ll)-2
    actual = base_ll.remove(expected)
    orig_data.pop(expected)
    assert(expected == actual)
    assert(len(base_ll) == orig_size-1)
    expected = 1
    actual = base_ll.remove(expected)
    orig_data.pop(expected)
    assert(expected == actual)
    assert(len(base_ll) == orig_size-2)
    assert(base_ll.peek_all() == orig_data)

def test_insert_and_remove():
    ll = LinkedList()
    ll.insert(0, 4)
    assert(ll.peek_all() == [4])
    ll.insert(1, 3)
    assert(ll.peek_all() == [4, 3])
    ll.insert(1, 2)
    assert(ll.peek_all() == [4, 2, 3])
    ll.insert(2, 0)
    assert(ll.peek_all() == [4, 2, 0, 3])
    ll.insert(0, 5)
    assert(ll.peek_all() == [5, 4, 2, 0, 3])
    expected = ll.remove(3)
    assert(expected == 0)
    assert(ll.peek_all() == [5, 4, 2, 3])
    expected = ll.remove(3)
    assert(expected == 3)
    assert(ll.peek_all() == [5, 4, 2])
    ll.insert(1, 0)
    assert(ll.peek_all() == [5, 0, 4, 2])