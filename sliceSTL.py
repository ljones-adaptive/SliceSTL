#!/usr/bin/python

import os
import sys, getopt
import string
from vertex import * 
from triangle import * 
from facet import * 

class STLFile():
    """
    """
	
    def __init__(self, filename, numberOfFacets):
        """
        """
        self.count = 0
        self.lines = []
        self.mydata = []
        self.title = None
        self.facetState = 0;
        self.filename = filename
        self.numberOfFacets = numberOfFacets
        
        self.inputfile = ''
        self.outputfile = ''
        
        try:
            opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
            print 'gcode.py -i <inputfile> -o <outputfile>'
            sys.exit(2)
        
        for opt, arg in opts:
            if opt == '-h':
                print 'gcode.py -i <inputfile> -o <outputfile>'
                sys.exit()
            elif opt in ("-i", "--ifile"):
                self.inputfile = arg
            elif opt in ("-o", "--ofile"):
                self.outputfile = arg


    def processFirstLine(self, line):
        """
        """
        line = line.replace("solid ",'')
    
    def processLastLine(self, line):
        """
        """
        line = line.replace("endsolid ",'')
        self.title = line
        
    def loadfacet(self, line):
        """
        """
        
        line = line.lstrip()
    	if line.startswith('solid'):
            self.processFirstLine(line)
        elif line.startswith('facet normal'):
            line = line.replace("facet normal ",'')
            linex, liney, linez = line.split(' ',2)
            facet = Facet()
            facet.setNormal(linex, liney, linez)
            self.mydata.append(facet)
            self.facetState = 1
        elif line.startswith('outer loop'):
            line = line.replace("outer loop ",'')
	elif line.startswith('vertex'):
	    line = line.replace("vertex ",'')
	    linex, liney, linez = line.split(' ',2)
            self.mydata[self.count].setNextTrianglePoint(linex, liney, linez)
	    self.facetState = self.facetState + 1;
	elif line.startswith('endloop'):
	    self.facetState = 0
	    self.count = self.count + 1
	elif line.startswith('endfacet'):
	    self.facetState = 0
    	elif line.startswith('endsolid'):
    	    self.processLastLine(line)

    def loadfile(self):
        """
        """
    
        # Open the file with read only permit
        print"opening file: %s" %(self.filename)
        f = open(self.filename, 'r')
        
        # Read the first line 
        line = f.readline()
        
        # If the file is not empty keep reading line one at a time
        # till the file is empty
        while line:
            self.lines.append(line)
            self.loadfacet(line)
            line=f.readline()
            
        f.close()
    
    def processfile(self):
        """
        """
        
        f = open('/home/ljones/stl Files/python/openscad.scad', 'w')
        
        count = 0
        for facet in self.mydata:
            facet.boundaries()
            facet.openScadFacetPrint(f)
            count = count + 1
            if int(self.numberOfFacets) == count :
		break
	f.close()

    def savefile(self):
        """
        """
#        for facet in self.mydata:
#            facet.printFacet()

    def main(self):
        """
        """

        print'--------------------------------------'
        self.loadfile()
        self.processfile()
        self.savefile()
        print'--------------------------------------'
  
if __name__ == "__main__":
        myfile = STLFile(sys.argv[1:]); 
        myfile.main()

