#!/usr/bin/python

from vertex import *  

class Triangle():
    def __init__(self):	
        self.vertices = []
        
    def addVertex(self, x, y, z):
        if len(self.vertices) > 3:
            raise("Too Many Vertex for a Triangle")
        vertex = Vertex()
        vertex.setPoints(x,y,z)
        self.vertices.append(vertex)
    
    def printVertices(self):
        for vertex in self.vertices:
            vertex.printPoints()

    def printVertex(self, number):
        if number > len(self.vertices):
            raise("Too Many Vertex to Print")
        self.vertices[number-1].printPoints()

    def returnVertex(self, number):
        if number > len(self.vertices):
            raise("Request for non existant Vertex")
        return (self.vertices[number-1].returnPoints())

if __name__ == "__main__":
    triangle = Triangle()
    triangle.addVertex(0, 0, 0)
    triangle.addVertex(0, 0, 10)
    triangle.addVertex(0, 10, 10)
    triangle.printVertices()
