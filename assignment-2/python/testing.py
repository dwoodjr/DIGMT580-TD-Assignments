import os
import site
import sys

os.environ["MAYA_LOCATION"] = "E:\\Program Files\\Autodesk\\Maya2023\\bin"
os.environ["PATH"] = "E:\\Program Files\\Autodesk\\Maya2023\\bin;" + os.environ["PATH"]
site.addsitedir("E:\\Program Files\\Autodesk\\Maya2023\\Python\\Lib\\site-packages")
site.addsitedir("E:\\Program Files\\Autodesk\\Maya2023\\Python\\DLLs")

'''
mayaDllPath = "E:\\Program Files\\Autodesk\\Maya2023\\Python\\DLLs"
mayaSitePath = "E:\\Program Files\\Autodesk\\Maya2023\\Python\\DLLs"
sys.path.append(mayaDllPath)
sys.path.append(mayaSitePath)
'''

import argparse
parser = argparse.ArgumentParser(description="Enter the Height and Radius of the cylinder.")
parser.add_argument("height", type = float, default = 5, help = "The height of the cylinder")
parser.add_argument("radius", type = float, default = 2, help = "The radius of the cylinder")

args = parser.parse_args()


import maya.standalone
maya.standalone.initialize(name = "python")

import maya.cmds as cmds

def create_polygon_cylinder():
    print("creating a cylider with a height of {} and a radius of {}".format(args.height, args.radius))  
    cmds.polyCylinder(ch = True, o = True, h = args.height, r = args.radius, sx = 25, sy = 25, sz = 25)

create_polygon_cylinder(5,10)
cmds.file(rename = "cyliner.ma")
cmds.file(save = True, type = "mayaAscii")
    