from math import pi

class Vertex(object):
    """
    A vertex of the hexglobe
    
    Attributes
    ----------
    lat: float
        The vertex latitude in degrees. 90.0 is the north pole/positive axis of
        rotation, -90.0 is the south pole/negative axis of rotation, and 0.0 is
        the equator/plane of rotation.
    long: float
        The vertex longitude in degrees. A floating point value between -180.0 
        and 180.0. 0.0 is set arbitrarily. On Earth, the line of 0.0 longitude 
        runs through Greenwich, England for some reason.
    rlat: float
        The vertex latitude in radians.
    long: float
        The vertex longitude in radians.
    """
    def __init__(self,latitude:float,longitude:float)->None:
        self.lat=latitude
        self.long=longitude
        self.rlat=pi*self.lat/180.0
        self.rlong=pi*self.long/180.0
        