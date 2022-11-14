'''
This script creates a maya file (in Ascii format)
and opens it for the user. 
'''
import maya.standalone
maya.standalone.initialize(name = "python")

import maya.cmds as cmds
import os

path = os.environ.get('MAYA_UI')
filePath = '{}\cubeUI.ma'.format(str(path))

def save_file():
    cmds.file(rn='{}\cubeUI.ma'.format(str(path)))
    cmds.file(force=True, save=True, type='mayaAscii')

def open_file():
    os.system('"{}"'.format(filePath))

save_file()
open_file()