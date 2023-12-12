class Face(object):
    """
    A Generic Face object
    
    Attributes
    ----------
    vertices: List[Vertex]
        A list of the vertices that bound the polygonal face, ideally ordered 
        counter-clockwise around the surface normal
    connections: List[Face]
        A list of faces neighboring this face ate the same detail level
    detail: int
        The detail level of this face or the layer in the search tree
    """
    def __init__(self) -> None:
        self.vertices = None
        self.connections = None
        self.detail = 0




