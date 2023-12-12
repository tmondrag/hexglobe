from .vertex import Vertex
    
class Face(object):
    vertices = None
    connections = None
    
class PFace(Face):
    vertices = [Vertex(),Vertex(),Vertex(),Vertex(),Vertex()]
    connections = [Face(),Face(),Face(),Face(),Face()]
    
class HFace(Face):
    vertices = [Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()]
    connections = [Face(),Face(),Face(),Face(),Face(),Face()]

class Hexglobe(object):
    faces = [PFace(),
             HFace(),HFace(),HFace(),HFace(),HFace(),
             PFace(),HFace(),PFace(),HFace(),PFace(),HFace(),PFace(),HFace(),PFace(),HFace(),
             PFace(),HFace(),PFace(),HFace(),PFace(),HFace(),PFace(),HFace(),PFace(),HFace(),
             HFace(),HFace(),HFace(),HFace(),HFace(),
             PFace()]
    