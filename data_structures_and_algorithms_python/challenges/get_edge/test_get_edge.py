import pytest
from get_edge import get_edges


class TestGetEdges:

    def test_proof_of_life(self):
        assert Graph
        assert get_edges

    @pytest.fixture()
    def graph(self):
        graph = Graph()

        # Create nodes
        vertex_1 = graph.add_vertex(1)
        vertex_2 = graph.add_vertex(2)
        vertex_3 = graph.add_vertex(3)
        vertex_4 = graph.add_vertex(4)
        vertex_5 = graph.add_vertex(5)
        vertex_6 = graph.add_vertex(6)

        # Create edges
        graph.add_edge(vertex_1, vertex_2, 150)
        graph.add_edge(vertex_2, vertex_1, 150)
        graph.add_edge(vertex_1, vertex_3, 82)
        graph.add_edge(vertex_3, vertex_1, 82)
        graph.add_edge(vertex_2, vertex_3, 99)
        graph.add_edge(vertex_3, vertex_2, 99)
        graph.add_edge(vertex_2, vertex_4, 42)
        graph.add_edge(vertex_4, vertex_2, 42)
        graph.add_edge(vertex_3, vertex_4, 105)
        graph.add_edge(vertex_4, vertex_3, 105)
        graph.add_edge(vertex_3, vertex_5, 37)
        graph.add_edge(vertex_5, vertex_3, 37)
        graph.add_edge(vertex_3, vertex_6, 26)
        graph.add_edge(vertex_6, vertex_3, 26)
        graph.add_edge(vertex_5, vertex_6, 250)
        graph.add_edge(vertex_6, vertex_5, 250)
        graph.add_edge(vertex_4, vertex_6, 73)
        graph.add_edge(vertex_6, vertex_4, 73)

        return graph

    test_data = (
        # Pass
        ([1, 2, 3], (True, '$249')),
        ([1, 2, 4], (True, '$192')),
        ([1, 3, 6, 5], (True, '$358')),
        ([3, 2, 4, 6], (True, '$214')),
        ([5, 6, 3, 2], (True, '$375')),

        # Fail
        ([1, 2, 5], (False, '$0')),
        ([4, 3, 1, 5], (False, '$0')),
        ([2, 6], (False, '$0')),
        ([6, 3, 5, 1], (False, '$0')),
        ([2, 3, 4, 5], (False, '$0')),

    )

    @pytest.mark.parametrize('input, output', test_data)
    def test_get_edges(self, input, output, graph):
        assert get_edges(graph, input) == output






        # ---------------------------------
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
    




