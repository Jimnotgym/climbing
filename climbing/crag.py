import json
import csv
import os

def readJSON(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data

class Crag():
    """class to hold all of the data about a crag
    """
    def __init__(self,name,path,description='no description',access='no details',mapsrc='',maphref=''):
        self.name=name
        self.description=description
        self.access=access
        self.mapsrc=mapsrc
        self.maphref=maphref
        self.path=path
        self.areas=Areas(self.path).areas



class Areas():
    """class to hold areas within a crag
    """
    def __init__(self,path):
        self.path=path
        self.getAreas()


    def getAreas(self):
        """Returs a list of dictionaries containing the area info"""
        self.areas=[]
        for areadir in os.listdir(self.path):

            try:
                # TODO This needs to use OS  join paths
                area=readJSON(self.path+'/'+areadir+'/area.json')
                self.areas.append(area)
            except NotADirectoryError:
                pass #skip crag files
        return self.areas

    def getAreaNames(self):
        """returns a list of area names"""
        # TODO put the areas in order
        self.names=[]
        for x in range (0, len(self.areas)):
            self.names.append(self.areas[x]['name'])
        return self.names




class Climb(list):
    """ base class for a climbs in an area
    """
    def __init__(self,path):
        with open('crags/'+path+'/climbs.csv', 'r') as f:
            reader = csv.reader(f)
            self.climbs = list(reader)
    def name(self,index):
        """Takes an int returns the name for that climb"""
        return self.climbs[index][0]
    def grade(self,index):
        """Takes an int returns the grade for that climb"""
        return self.climbs[index][1]
    def description(self,index):
        """Takes an int returns the description for that climb"""
        return self.climbs[index][2]
    def names(self):
        """Returns a list of names"""
        namelist=[]
        for x in range (0,len(self.climbs)):
            namelist.append(self.climbs[x][0])
        return namelist
