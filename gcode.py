#!/usr/bin/python

import os
import sys
import string

class Gcode():
    """
    """
	
    def __init__(self):
        """
        """
        self.redirectToFile = 0
        self.filename = None
        self.redirectfilehandle = None

    def GcodeRedirectFileName(self, filename):
        """
        """
        self.filename = filename
        
    def GcodeRedirectStart(self):
        """
        """
        self.redirectToFile = 1
        if self.redirectfilehandle is None and self.filename is not None:
            self.redirectfilehandle = open(self.filename, 'r')
        
    def GcodeRedirectStop(self):
        """
        """
        self.redirectToFile = 0
        if self.redirectfilehandle is not None:
            self.redirectfilehandle.close()
            self.redirectfilehandle = None
            self.filename = None
            
    def Gcode_Print(self, gCodeString):
        """
        """
        print"%s" % (gCodeString)
        if self.redirectToFile == 1 and self.redirectfilehandle is not None:
            self.redirectfilehandle.write(gCodeString)
        
    def Gcode_Absolute(self):
        """
        """
        self.Gcode_Print("G90            ; Switch to absolute movement")

    def Gcode_Millimenters(self):
        """
        """
        self.Gcode_Print("G21            ; Units to Millimenters")        

    def Gcode_Home(self):
        """
        """
        self.Gcode_Print("G28            ; Move to the home position")        

    def Gcode_Relative(self):
        """
        """
        self.Gcode_Print("G91            ; Switch to relative movement")

    def Gcode_DisableMotors(self):
        """
        """
        self.Gcode_Print("M84            ; disable motors")
        

    def Gcode_ExtruderTemp(self, temp):
        """
        """
        print("M104 S%d        ; Set extruder Temperature" % (temp))

    def Gcode_ExtruderTempOff(self):
        """
        """
        self.Gcode_ExtruderTemp(0)

    def Gcode_BedTemp(self, temp):
        """
        """
        str ="M140 S%d        ; Set Bed Temperature" % (temp)
        self.Gcode_Print(str)

    def Gcode_FanOff(self):
        """
        """
        self.Gcode_Print("M107           ; Fan Off")
        
    def Gcode_Wait(self):
        """
        """
        self.Gcode_Print("M116           ; Wait for both temperatures to be met")
        
    def Gcode_WaitTemperatureBed(self, temp):
        """
        """
        str ="M190 S%d          ; Wait for both temperatures to be met" % (temp)
        self.Gcode_Print(str)
        
    def Gcode_SetPosition(self, x=None, y=None, z=None, e=None):
        """
        """
        str = "G92 "
        if x is not None:
            str += "X%f " % (x)
        if y is not None:
            str += "Y%f " % (y)
        if z is not None:
            str += "Z%f " % (z)
        if e is not None:
            str += "E%f " % (e)
        self.Gcode_Print(str)
        
    def Gcode_ControlMove(self, x=None, y=None, z=None, e=None, f=None):
        """
        """
        str = "G1 "
        if x is not None:
            str += "X%f " % (x)
        if y is not None:
            str += "Y%f " % (y)
        if z is not None:
            str += "Z%f " % (z)
        if e is not None:
            str += "E%f " % (e)
        if f is not None:
            str += "F%f " % (f)
        self.Gcode_Print(str)
        
    def Gcode_ (self):
        """
        """
        self.Gcode_Print("")
        
    def start_code(self):
        """
        """
        self.Gcode_Millimenters()
        self.Gcode_FanOff()
        self.Gcode_Absolute()
        self.Gcode_Millimenters()
        self.Gcode_Home()
        self.Gcode_SetPosition(x=None, y=None, z=None, e=0)
        self.Gcode_WaitTemperatureBed(56)
        self.Gcode_BedTemp(60)
        self.Gcode_ExtruderTemp(180)
        self.Gcode_Wait()
        self.Gcode_ControlMove(x=0, y=130, z=None, e=None, f=1000)
        self.Gcode_Absolute()
        self.Gcode_SetPosition(x=None, y=None, z=None, e=0)

    def end_code(self):
        """
        """
        self.Gcode_SetPosition(x=None, y=None, z=None, e=0)
        self.Gcode_Relative()
        self.Gcode_ControlMove(x=None, y=None, z=None, e=-5.0, f=100)
        self.Gcode_ControlMove(x=None, y=None, z=10, e=None, f=1000)
        self.Gcode_Absolute()
        self.Gcode_ControlMove(x=12, y=None, z=None, e=None, f=4000)
        self.Gcode_ControlMove(x=None, y=130, z=None, e=None, f=1000)
        self.Gcode_ExtruderTempOff()
        self.Gcode_BedTemp(0)
        self.Gcode_DisableMotors()

    def outputGcode(self):
        """
        """
        self.GcodeRedirectFileName('/home/ljones/stl Files/python/openscad.scad')
        self.GcodeRedirectStart()
        self.start_code()
        self.Gcode_Print(";---------------------------------------------------")
	self.printLayer()
        self.Gcode_Print(";---------------------------------------------------")
        self.end_code()
        self.GcodeRedirectStop()
        
    def printLayer(self):
        """
        """
        self.Gcode_ControlMove(x=None, y=None, z=0.2, e=None, f=7800)
        self.Gcode_ControlMove(x=43.87, y=56.57, z=None, e=None, f=None)

if __name__ == "__main__":
    gcode = Gcode()
    gcode.outputGcode()

