'''
This script creates a GUI to create a cube. 
'''
import maya.cmds as cmds

def geo_ui():
        
    global cubeCountField
    global cubeWidthField
    global cubeHeightField
    global cubeDepthField

    if (cmds.window("Make-a-Cube", exists=True)):
        cmds.deleteUI("Make-a-Cube")
    else:    
        geoUI = cmds.window(title='Make-a-Cube', widthHeight=(300, 200))
        cmds.columnLayout()
        cmds.text(label='Number of Cubes')
        cubeCountField = cmds.intField(min=1)
        cmds.text(label='Width of Cubes')
        cubeWidthField = cmds.floatField(min=0.5)
        cmds.text(label='Height of Cubes')
        cubeHeightField = cmds.floatField(min=0.5)
        cmds.text(label='Width of Cubes')
        cubeDepthField = cmds.floatField(min=0.5)
        cmds.text(label='Push this button to make a cube appear!')
        cmds.button(label='Make Cube(s)', command=buttonFunction)
        cmds.showWindow(geoUI)

def buttonFunction(*args):
    global cubeCountField
    global cubeWidthField
    global cubeHeightField
    global cubeDepthField
    
    numCubes = cmds.intField(cubeCountField, query=True, value=True)
    cubeWidth = cmds.floatField(cubeWidthField, query=True, value=True)
    cubeHeight = cmds.floatField(cubeHeightField, query=True, value=True)
    cubeDepth = cmds.floatField(cubeDepthField, query=True, value=True)
    
    for i in range(numCubes):
        cmds.polyCube(w=cubeWidth, h=cubeHeight, d=cubeDepth)
        cmds.move(((i * cubeDepth) * 2.5), 0, 0)
    
        
geo_ui()
