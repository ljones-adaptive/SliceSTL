#!/usr/bin/python

from triangle import * 

class Facet():
    def	__init__(self):
        """
        """
        self.normal   = Vertex ()
        self.triangle = Triangle() 
        
    def setNormal(self, x, y, z):
        """
        """
        self.normal.setPoints(float(x), float(y), float(z))

    def setNextTrianglePoint(self, x, y, z):
        """
        """
        self.triangle.addVertex(float(x), float(y), float(z))
	
    def printFacet(self):
        """
        """
        self.normal.printPoint()
        self.triangle.printVertices()
        
    def CalculateLowestPoint(self):
        """
        """
        if len(self.triangle) is not 3:
    	    print"Incorrect number of triangle points"
        else:
            print"correct number of triangle points available"
        self.triangle.checkForHorizontal()
        

    def openScadFacetPrint(self, f):
        """
        """
        
        mystr = 'polyhedron(points=['
        
        for index in range(0, 3):
            x, y, z = self.triangle.returnVertex(index)
            mystr += '[%d,'  % (float(x))
            mystr +=  '%d,'  % (float(y))
            mystr +=  '%d],' % (float(z))

        mystr = mystr[:-1]
	mystr += '], triangles=[[0,1,2]]);\n'
        	
        f.write(mystr)
	
    def boundaries(self):
        """
        """
        
#        x = []
#        y = []
#        z = []
#        for index in range(0, 3):
#            x, y, z = self.triangle.returnVertex(index)

#        x.append(vertex['x'])
#        y.append(vertex['y'])
#        z.append(vertex['z'])
            
#        x.sort()
#        self.minx = x[0] 
#        self.maxx = x[2]
        
#        y.sort()
#        self.miny = y[0]
#        self.maxy = y[2]
        
#        z.sort()
#        self.minz = z[0]
#        self.maxz = z[2]
        
#        print ('Boundaries: x-min %f, x-max %f' % (self.minx, self.maxx))
#        print ('Boundaries: y-min %f, y-max %f' % (self.miny, self.maxy))
#        print ('Boundaries: z-min %f, z-max %f' % (self.minz, self.maxz))
        
if __name__ == "__main__":
    facet = Facet()
    facet.setNormal(-1, 0, 0)
    
    facet.setNextTrianglePoint(0, 0, 10)
    facet.setNextTrianglePoint(0, 10, 10)
    facet.setNextTrianglePoint(0, 0, 0)
    
    facet.printFacet()
    facet.CalculateLowestPoint()

