class Vertex:

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return self.val

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val})'


class Edge:
    def __init__(self, vertex: Vertex, weight: int) -> None:
        self.vertex = vertex
        self.weight = weight


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, val):
        vertex = Vertex(val)
        self.adjacency_list[vertex] = []
        return vertex
    
    def add_edge(self, start: Vertex, end: Vertex, weight: int = 1) -> None:
        if start not in self.adjacency_list:
            raise KeyError('Start Vertex is not in the Graph')
        if end not in self.adjacency_list:
            raise KeyError('End Vertex is not in the Graph')

        edge = Edge(end, weight)
        adjacencies = self.adjacency_list[start]
        adjacencies.append(edge)

    def get_nodes(self):

        return set(self.adjacency_list.keys())

    def get_neighbors(self, vertex):

        if not vertex in self.adjacency_list:
            raise KeyError('Given Vertex is not in the Graph')

        edges = self.adjacency_list[vertex]

        return [{'vertex': edge.vertex,
                 'weight': edge.weight} for edge in edges]

    def breadth_first(self, start):

        q = Queue()
        output = set()

        if not start in self.adjacency_list:
            raise KeyError('Given Vertex is not part of the Graph')

        q.enqueue(start)

        while not q.is_empty():
            vertex = q.dequeue()
            output.add(vertex)

            for neighbor in self.get_neighbors(vertex):
                if neighbor['vertex'] not in output:
                    q.enqueue(neighbor['vertex'])

        return output

    def pre_order(self, start, output):
        if output is None:
            output = set()

        if start in self.adjacency_list:
            output.add(start)
        else:
            raise KeyError('Given Vertex is not part of the Graph')

        for edge in self.adjacency_list[start]:
            output = self.pre_order(edge.vertex, output)

        return output

    def size(self):

        return len(self.get_nodes())



# -------------------------------------  
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
 

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
      