#!/usr/bin/python

class Vertex():
    def __init__(self, x=None, y=None, z=None):	
        self.x = x        
        self.y = y        
        self.z = z
        
    def setPoints(self, x, y, z):
        self.x = x        
        self.y = y        
        self.z = z
        
    def returnPoints(self):
        return (self.x, self.y, self.z)
       
    def printPoint(self):
        print "x=%f, y=%f, z=%f" % (self.x, self.y, self.z)
       
if __name__ == "__main__":
    vertex = Vertex()
    vertex.setPoints(0, 0, 0)
    vertex.printPoint()
