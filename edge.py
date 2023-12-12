from .vertex import Vertex

class Edge(object):
    """
    An edge object in the graph defining a hexglobe. An edge is unidirectional 
    and points from a tail vertex to a head vertex.
    
    Attributes
    ----------
    head: Vertex
        The vertex that serves as one bound of the edge. If traversing edges 
        counterclockwise around a face's boundary, it is the second of the 
        edge's vertices to be encountered.
    tail: Vertex
        The vertex that serves as one bound of the edge. If traversing edges 
        counterclockwise around a face's boundary, it is the first of the 
        edge's vertices to be encountered.
    face: Face
        The face bounded by the edge and the vertices.
    prev: Edge
        A neighoring edge that bounds the same face. The head of the prev edge 
        should be the tail of this edge.
    next: Edge
        A neighoring edge that bounds the same face. The head of this edge 
        should be the tail of the next edge.
    twin: Edge
        A neighoring edge that is antiparallel. The head of this edge should 
        be the tail of the twin edge and the tail of this edge should be the 
        head of the twin edge.
    detail: int
        The detail level of this edge or the layer in the search tree.
    idx: int
        This edge's index on the edge list for quicker reference afterward.
    """
    def __init__(self, tail:Vertex, head:Vertex) -> None:
        self.head = head
        self.tail = tail
        self.face = None
        self.prev = None
        self.next = None
        self.twin = None
        self.detail = 0
        self.idx = None

class EdgeList(list):
    """
    A list of edges. A list structure with extra edge related methods
    """
    def fetch_twin(self,idx:int) -> Edge:
        """
        Return self[idx].twin if it is not None, otherwise raise an RuntimeError
        """
        twin = self[idx].twin
        if twin is None:
            raise RuntimeError(f"Error: edge {idx} has no twin.")
    
    def appendIsolatedEdge(self,tail:Vertex, head:Vertex) -> None:
        """
        Append an isolated edge and it's twin to the edge list. The edge is 
        disconnected from everything else except it's twin and it's vertices. 
        I don't know why you would want to do this.
        """
        primo = Edge(tail,head)
        segundo = Edge(head,tail)
        primo.twin = segundo
        primo.prev = segundo
        primo.next = segundo
        primo.idx = len(self)
        segundo.twin = primo
        segundo.prev = primo
        segundo.next = primo
        segundo.idx = len(self)+1
        self.append(primo)
        self.append(segundo)
        