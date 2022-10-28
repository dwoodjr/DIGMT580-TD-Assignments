from hou_setup import enableHouModule           
enableHouModule()


import hou
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('job', help='path to the project directory')
parser.add_argument('geo', help='path to the .bgeo geometry object')
args = parser.parse_args()

#Create a geometry node parent at the object level in houdini
OBJ = hou.node('/obj')
geo = OBJ.createNode('geo')
#create a file node inside the parent geometry node
file = geo.createNode('file')
file.parm('file').set(args.geo)

fileGeo = hou.pwd().geometry()
pts = fileGeo.points()

hou.hipFile.save(file_name = '{}/test.hipc'.format(args.job))