from tree import Node , BinaryTree , BinarySearchTree
import pytest 

@pytest.fixture
def prep():
    Binary_tree = BinaryTree()
    Binary_tree.root = Node(3)
    Binary_tree.root.right = Node(4)
    Binary_tree.root.left = Node(1)
    Binary_tree.root.right.left = Node(2)
    return Binary_tree


def test_preorder(prep):
    actual = prep.preorder()  
    expected = [3,1,4,2]  
    assert actual == expected 

def test_contains():
    Binary_tree = BinarySearchTree()
    Binary_tree.add(2)
    assert Binary_tree.root.value == 2
    
