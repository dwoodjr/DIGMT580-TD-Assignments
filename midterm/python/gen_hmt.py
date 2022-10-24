import hou
import math

'''
#setup object and geometry nodes
'''
#object scene root
#node = hou.pwd()
OBJ = hou.node('/obj') 
geo = OBJ.createNode('geo')



#create attribute values
note = geo.addAttrib(hou.attribType.Point, "note", 0)
duration = geo.addAttrib(hou.attribType.Point, "duration", 0.0)
time = geo.addAttrib(hou.attribType.Point, "time", 0.0)
velocity = geo.addAttrib(hou.attribType.Point, "vel", 1.0)
channel = geo.addAttrib(hou.attribType.Point, "channel", 0)


#Set point attribute values
for point in geo.points():
    point.setAttribValue("note", point.attribValue("py_i"))
    point.setAttribValue("time", point.attribValue("px"))
    point.setAttribValue("duration", 2.0)
    point.setAttribValue("vel", 1.0)
    point.setAttribValue("channel", 8)   