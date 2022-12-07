import math
import random

geo = hou.pwd().geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.
points = geo.points()


#create attribute values
note = geo.addAttrib(hou.attribType.Point, "note", 0)
duration = geo.addAttrib(hou.attribType.Point, "duration", 0.0)
time = geo.addAttrib(hou.attribType.Point, "time", 0.0)
velocity = geo.addAttrib(hou.attribType.Point, "vel", 1.0)
channel = geo.addAttrib(hou.attribType.Point, "channel", 0)

chanNumMax = hou.parm("../chanNumMax").eval()
chanNumMin = hou.parm("../chanNumMin").eval()
durMax = hou.parm("../durMax").eval()
durMin = hou.parm("../durMin").eval()
velMax = hou.parm("../velMax").eval()
velMin = hou.parm("../velMin").eval()


#Set point attribute values
for point in points:
    '''
    setup Px, Py, and Pz values to use in attributes
    '''
    pos = point.position()
    px = pos[0]
    py = pos[1]
    pz = pos[2]
    
    '''
    set required point parameters for midi sends
    '''
    point.setAttribValue("note", (int(py)))
    point.setAttribValue("time", px)
    point.setAttribValue("duration", random.uniform(durMin, durMax))
    point.setAttribValue("vel", random.uniform(velMin, velMax))
    point.setAttribValue("channel", random.randint(chanNumMin, chanNumMax))  
        
