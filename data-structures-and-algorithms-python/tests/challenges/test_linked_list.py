from  data.challenges.linked_list.linked_list import LinkedList
import 
pytest

def test_none():
    list = LinkedList()
    assert list.head == None

def test_insert():
    list = LinkedList()
    list.insert(3)
    assert list.head.value == 3

def test_head():
    list = LinkedList()
    list.insert(3)
    assert list.head.value == 3

def test_insert_Numbers():
    list = LinkedList()
    list.insert(3)
    list.insert(5)
    list.insert(7)
    list.insert(9)
    assert list.head.value == 9
    assert list.head.next.value == 7
    assert list.head.next.next.value == 5
    assert list.head.next.next.next.value == 3
    assert list.head.next.next.next.next == None

def test_includes_true():
    list = LinkedList()
    list.insert(7)
    list.insert(9)
    assert list.includes(9) == True

def test_includes_false():
    list = LinkedList()
    list.insert(7)
    list.insert(9)
    assert list.includes(5) == False

def test_str():
    list = LinkedList()
    list.insert(3)
    list.insert(5)
    list.insert(7)
    list.insert(9)
    assert list.__str__() == "{ 9 } -> { 7 } -> { 5 } -> { 3 } -> NULL"
