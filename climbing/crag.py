import json

def ReadJSON(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data


class Crag():
    """ class to hold all of the data about a crag
    """
    def __init__(self,**kwargs):
        self.description=description
        self.access=access
        self.mapsrc=mapsrc
        self.maphref=maphref


class Climbs():
    """Object to hold the climbs for a Crag
    """
    
