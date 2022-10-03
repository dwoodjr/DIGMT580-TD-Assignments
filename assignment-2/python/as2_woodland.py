import argparse
import maya.cmds as cmds
  
parser = argparse.ArgumentParser(description="Enter the Height and Radius of the cylinder.")
parser.add_argument("height", type = float, default = 5, help = "The height of the cylinder")
parser.add_argument("radius", type = float, default = 2, help = "The radius of the cylinder") 
args = parser.parse_args()

def create_rope(height, radius):
    print("A cylinder with a height of {} and a radius of {} will be created!".format(args.height, args.radius))
    cmds.polyCylinder(ch = True, o = True, h = height, r = radius, sx = 25, sy = 25, sz = 25)
    print("Cylinder created!")

print("Script imported!")
 