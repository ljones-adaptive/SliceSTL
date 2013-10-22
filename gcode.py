#!/usr/bin/python

class Gcode():
    """
    """
	
    def __init__(self):
        """
        """

    def Gcode_Absolute(self):
        """
        """
        print"G90              ; Switch to absolute movement"

    def Gcode_Millimenters(self):
        """
        """
        print"G21              ; Units to Millimenters"        

    def Gcode_Home(self):
        """
        """
        print"G28              ; Move to the home position"        

    def Gcode_Relative(self):
        """
        """
        print"G91            ; Switch to relative movement"        

    def Gcode_DisableMotors(self):
        """
        """
        print"M84            ; disable motors"
        

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
        print("M140 S%d        ; Set Bed Temperature" % (temp))

    def Gcode_FanOff(self):
        """
        """
        print"M107              ; Fan Off"
        
    def Gcode_Wait(self):
        """
        """
        print"M116             ; Wait for both temperatures to be met"
        
    def Gcode_WaitTemperatureBed(self, temp):
        """
        """
        print("M190 S%d          ; Wait for both temperatures to be met" % (temp))
        
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
        print str
        
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
        print str
        
    def Gcode_ (self):
        """
        """
        print""
        
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
        self.start_code()
        self.printLayer()
        self.end_code()
        
    def printLayer(self):
        """
        """
        self.Gcode_ControlMove(x=None, y=None, z=0.2, e=None, f=7800)
        self.Gcode_ControlMove(x=43.87, y=56.57, z=None, e=None, f=None)

if __name__ == "__main__":
    gcode = Gcode()
    gcode.outputGcode()

