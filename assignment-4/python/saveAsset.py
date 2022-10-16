'''
This script takes five arguments. 
(1) A project / environment variable name. (2) The name of an asset. 
(3) The type of the asset
(4) The name of the artist. (5) The current version number of teh asset.
This script defines an asset file name using the above arguments 
and increments the version number with each save.
The project name is used to access the environment variable value 
and save the file to that directory.
'''

import maya.standalone
maya.standalone.initialize()

import os
import argparse
import maya.cmds as cmds

# Define the argument parser and arguments
parser = argparse.ArgumentParser()
parser.add_argument('project_name', help='Name of the project (same as env var)')
parser.add_argument('asset_name', help='Name of the asset')
parser.add_argument('asset_type', help='Type of asset')
parser.add_argument('artist_name', help='Name of the artist')
parser.add_argument('version_number', help='Current version number of the asset')

# Assign arguments to usable variables
args = parser.parse_args()
project_name = args.project_name
asset_name = args.asset_name
asset_type = args.asset_type
artist_name = args.artist_name
version_number = args.version_number

#find the env var value of the project 
env_var = os.environ.get(project_name)
#print(env_var)

def saveFile():
    #call version num as global variable
    global version_number
    #increment the version number
    version_number = int(version_number) + 1
    #create the name for the asset file and path for asset
    save_file_name = asset_name + '.' + asset_type + '.' + artist_name + '.' + str(version_number) + '.ma'
    save_path = os.path.join(env_var, save_file_name)
    #save the file using maya cmds
    cmds.file(rn = save_path)
    cmds.file(save=True, type='mayaAscii')
    #check version number and confirm file is saved
    #print(version_number)
    print(save_file_name + ' was saved!')

#run save asset file function
saveFile()