from hou_setup import enableHouModule           
enableHouModule()

import hou
import argparse
'''
#setup object and geometry nodes
'''
parser = argparse.ArgumentParser()
parser.add_argument('job', help='path to the project directory')
parser.add_argument('geo', help='path to the .bgeo geometry object')
args = parser.parse_args()

'''
#setup object and geometry nodes
'''
#Create a geometry node parent at the object level in houdini
OBJ = hou.node('/obj')
geo = OBJ.createNode('geo')
#create a file node inside the parent geometry node
file = geo.createNode('file')
file.parm('file').set(args.geo)

#from pt_parm import all
#get points from read in geometry
pyNode = file.createOutputNode('python')
f = open('pt_parm.txt', 'r')
pyNode.parm('python').set(f.read())

    
hou.hipFile.save(file_name = '{}/hmtNotes.hipc'.format(args.job))