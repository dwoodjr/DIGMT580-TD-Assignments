import os
import sys
import argparse

'''
This script sets the project directory 
and environment variable to specified path
'''
parser = argparse.ArgumentParser()
parser.add_argument('path', help='enter project path')
args = parser.parse_args()

path = args.path + '\mayaUI'
env = 'MAYA_UI'

def set_env():
    if os.environ.get('MAYA_UI'):
        print('Environment variable exists')
    else:    
        print('Environment variable does not exist...creating')
        os.environ['MAYA_UI'] = path
        os.system('SETX {0} "{1}"'.format(env,path))
        print('MAYA_UI set to {}'.format(path))
        
        print(os.environ.get('MAYA_UI'))

def create_dir(): 
    os.makedirs(path)
    print('A Directory has been created: {}'.format(path))

def run_mayapy():
    os.system('mayapy')

set_env()
create_dir()
run_mayapy()