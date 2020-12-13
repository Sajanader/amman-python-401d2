class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise AttributeError('Cannot be called an empty stack')
        else:
            remved_top = self.top.value
            self.top = self.top.next 
            return remved_top
         
    def peek(self):
        if self.top == None:
            raise AttributeError('There is no peek in empty stack')
        return self.top.value
        
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False   

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        node = Node(data)
        if self.rear:
            self.rear.next= node
            self.rear = node
        else:
            self.front =node
            self.rear = node    

    def dequeue(self,data):
        if self.front:
            removed_front = self.front
            self.front = self.front.next
            return removed_front
        else:
            raise AttributeError('The Queue is empty')

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return 'There is no any peek becasue the Queue is empty'    

    def is_empty(self):
        if self.front == None:
           return True
        else:
            return False

class PseudoQueue:
        def __init__(self):
            self.stack1 = Stack()
            self.stack2 = Stack()
        
        def enqueue(self,data):
            self.stack1.push(data)
            
        def dequeue(self):
            if self.stack1.is_empty() and self.stack2.is_empty():
                raise AttributeError('The PseudoQueue is empty') 
            if self.stack2.is_empty():
                while self.stack1.top:
                      self.stack2.push(self.stack1.pop())
                return self.stack2.pop()
            else:
                return self.stack2.pop()    

                
    
      



      




    
             



     
               