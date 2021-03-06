""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e
    
    def get_edge(self, v, w):
        try:
            return self[v][w]
        except:
            return None

    def remove_edge(self, e):
        v, w = e
        try:
            del(self[v][w])
            del(self[w][v])
        except:
            print("The edge doesn't exist")

    def vertices(self):
        return [key for key, value in self.items()]
    
    def edges(self):
        edge_list = []
        if len(self) > 2:
            for key, value in self.items():
                for vertex, edge in value.items():
                    if edge not in edge_list:
                        edge_list.append(edge)
        return edge_list

    def out_vertices(self, v):
        [(vertex, edge)] = self[v].items()
        return vertex
    
    def out_edges(self, v):
        [(vertex, edge)] = self[v].items()
        return edge

    def add_all_edges(self):
        for v in self.vertices():
            other_verts = [x for x in self.vertices() if x != v]
            for vertex in other_verts:
                self.add_edge(Edge(v, vertex))
            

def main(script, *args):
    v = Vertex('v')
    print v
    w = Vertex('w')
    print w
    e = Edge(v, w)
    print e
    g = Graph([v,w], [e])
    print g
    test_edge = g.get_edge(v,w)
    print g.vertices()
    print g.edges()
    print g.out_vertices(v)
    print g.out_edges(v)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
