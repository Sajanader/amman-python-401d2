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

    def depth_first(self, start, output):
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
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next

class Queue:

    def __init__(self, val=None):
        self.front = self.rear = Node(val) if val else None

    def enqueue(self, val: any):
        if self.is_empty():
            self.front = self.rear = Node(val)
        else:
            new_node = Node(val)
            self.rear.next, self.rear = new_node, new_node

    def dequeue(self):
        if self.is_empty():
            raise AttributeError('Cannot be called on empty Queue')
        else:
            tmp = self.front.val
            self.front = self.front.next
            return tmp

    def peek(self):

        if self.is_empty():
            raise AttributeError('Cannot be called on empty Queue')
        else:
            return self.front.val

    def is_empty(self):
        return self.front is None