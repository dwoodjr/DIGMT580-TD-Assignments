import argparse

parser = argparse.ArgumentParser(description="Enter the Height and Radius of the cylinder.")
parser.add_argument("height", type = float, default = 5, help = "The height of the cylinder")
parser.add_argument("radius", type = float, default = 2, help = "The radius of the cylinder")
args = parser.parse_args()

print("The height of the cylinder will be: {}".format(int(args.height)))
print("The height of the cylinder will be: {}".format(int(args.radius)))
ht = args.height
rd = args.radius

import maya.cmds as cmds

print("creating a cylider with a height of {} and a radius of {}".format(args.height, args.radius))  
cmds.polyCylinder(ch = True, o = True, h = ht, r = rd, sx = 25, sy = 25, sz = 25)
cmds.file(rename = "cyliner.ma")
cmds.file(save = True, type = "mayaAscii")