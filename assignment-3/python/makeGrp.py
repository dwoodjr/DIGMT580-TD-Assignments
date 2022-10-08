import os
import maya.standalone
maya.standalone.initialize()

'''
This script creates a maya file (in Ascii format)
and makes an empty group with the name 'asset'.
The file is then saved to a directory.   
'''

import maya.cmds as cmds

#set variables
env = os.environ['asset']
name = str('asset')
#print(env)

def make_group():
    cmds.group(em=True, n=name)

def save_file():
    cmds.file(rn='{}/asset.ma'.format(str(env)))
    cmds.file(force=True, save=True, type='mayaAscii')
    
make_group()
save_file()