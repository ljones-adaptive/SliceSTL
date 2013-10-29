#!/usr/bin/python

from vertex import *  

class Triangle():
    """
    """
        
    def __init__(self):	
        """
        """
        self.vertices = []

    def __len__(self):
        """
        """
        return(len(self.vertices))        

    def addVertex(self, x, y, z):
        """
        """
        if len(self.vertices) > 3:
            raise("Too Many Vertex for a Triangle")
        vertex = Vertex()
        vertex.setPoints(x,y,z)
        self.vertices.append(vertex)
    
    def printVertices(self):
        """
        """
        for vertex in self.vertices:
            vertex.printPoint()

    def printVertex(self, number):
        """
        """
        if number > len(self.vertices):
            raise("Too Many Vertex to Print")
        self.vertices[number-1].printPoints()

    def returnVertex(self, number):
        """
        """
        if number > len(self.vertices):
            raise("Request for non existant Vertex")
        return (self.vertices[number-1].returnPoints())

    def checkForHorizontal(self):
        """
        """
        if len(self.vertices) < 3:
            raise("Too Many Vertex for a Triangle")
#        if self.vertices[0].z == self.vertices[1].z:
        print "Horizontal 1 %f %f" % (self.vertices[0].z, self.vertices[1].z)
#        if self.vertices[1].z == self.vertices[2].z:    
        print "Horizontal 2 %f %f" % (self.vertices[1].z, self.vertices[2].z)
#        if self.vertices[2].z == self.vertices[0].z:    
        print "Horizontal 3 %f %f" % (self.vertices[2].z, self.vertices[0].z)
        
if __name__ == "__main__":
    triangle = Triangle()
    triangle.addVertex(0, 0, 0)
    triangle.addVertex(0, 0, 10)
    triangle.addVertex(0, 10, 10)
    triangle.printVertices()
