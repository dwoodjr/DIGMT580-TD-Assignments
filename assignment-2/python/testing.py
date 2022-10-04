
'''
This script will create a cylinder that with a specified height and radius passed in as arguments through argparse
 
'''
#argparse setup
import argparse
parser = argparse.ArgumentParser(description="Enter the Height and Radius of the cylinder.")

#height and radius arguments
parser.add_argument("height", type = float, default = 5, help = "The height of the cylinder")
parser.add_argument("radius", type = float, default = 2, help = "The radius of the cylinder")

args = parser.parse_args()

#import and initialize maya standalone
import maya.standalone
maya.standalone.initialize(name = "python")

#import maya API commands
import maya.cmds as cmds

#function that creates a cylinder
def create_polygon_cylinder(height,radius):
    print("creating a cylider with a height of {} and a radius of {}".format(height,radius))  
    cmds.polyCylinder(ch = True, o = True, h = height, r = radius, sx = 25, sy = 25, sz = 25)

#call funtion 
create_polygon_cylinder(args.height,args.radius)

#rename a file and save it as maya ascii
cmds.file(rename = "cylinder.ma")
cmds.file(save = True, type = "mayaAscii")
    