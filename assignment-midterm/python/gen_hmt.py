from hou_setup import enableHouModule           
enableHouModule()

import hou
import argparse
'''
#setup arguments and parse
'''
parser = argparse.ArgumentParser()
parser.add_argument('job', help='path to the project directory')
parser.add_argument('geo', help='path to the .bgeo geometry object')
parser.add_argument('startNote', help='enter a midi note to start at, int from 0-127')
args = parser.parse_args()

'''
#setup object and geometry nodes for houdini file
'''
#Create a geometry node parent at the object level in houdini
OBJ = hou.node('/obj')
geo = OBJ.createNode('geo')
#create a file node inside the parent geometry node
file = geo.createNode('file', 'importGeo')
file.parm('file').set(args.geo)
#create a transform node to mode point cloud to new range
trans = file.createOutputNode('xform', 'moveMidiNotes')
trans.parm('ty').set(args.startNote)
trans.parm('tx').set(0.5)
#create python SOP and read in python from txt file
pyNode = trans.createOutputNode('python', 'noteAttribs')
f = open('pt_parm.txt', 'r')
pyNode.parm('python').set(f.read())
#create HMT midi output network
midiIO = pyNode.createOutputNode('hmt_midi_output', 'midiNotesOut')
midiIO = pyNode.createOutputNode('hmt_time_bar')

#save the processed geo to a hip (Houdini) file   
hou.hipFile.save(file_name = '{}/hmtNotes.hipc'.format(args.job))