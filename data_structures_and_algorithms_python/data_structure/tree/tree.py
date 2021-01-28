class Node:
    def __init__(self,value ):
        self.value  = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None 

    def preorder(self):
        array_of_output = [] 
        def _walk(node):
            array_of_output.append(node.value)
            if node.left:
               _walk(node.left)
            if node.right:
               _walk(node.right)  
        _walk(self.root)  
 
        return array_of_output 

    def inOrder(self):
        array_of_output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            array_of_output.append(node.value)
            if node.right:
                _walk(node.right)
            return array_of_output

        if self.root:    
            _walk(self.root)
        return array_of_output

    def postOrder(self):
        array_of_output = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            array_of_output.append(node.value)
            return array_of_output

        if self.root:    
            _walk(self.root)

        return array_of_output

    def max_value(self , root):  
        max_number = self.root.value
        def _closure(node):
            if node:
                if node.value > max_number:
                    max_number = node.value
                _closure(node.left)
                _closure(node.right)
                return max_number

        _closure(self.root)
        return max_number


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return 
                    else:
                        _walk(node.left) 
                else:
                    if not node.right:
                        node.right = Node(value)
                        return 
                    else:
                        _walk(node.right)
                _walk(self.root)

    def contains(self, value):
        if self.root.value == value:
            return True
        elif self.root.value < value:
            return self.root.right.value == value 
        else:
            return self.root.right.value == value      
    


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    print(bt.preorder())
    print(bt.max_value(bt.root))
 



