
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else: 
            node.next = self.head
            self.head = node
        
    def includes(self, data):
        current = self.head
        while (current != None):
            if current.value == data:
                return True
            else:
                current = current.next
        return False
            
    def __str__(self):
        if self.head == None:
            return ("NULL")
        else:
            list = ""
            current = self.head
            while (current != None):
                list += '{ %s } -> ' %current.value
                current = current.next
            list += 'NULL'
            return (f"{list}")

if __name__ == "__main__":
    myList = LinkedList()
    myList.insert(5)
    myList.insert(3)
    myList.insert(1)
    print(myList)
    print(myList.includes(10))
