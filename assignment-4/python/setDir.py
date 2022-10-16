'''
This script takes in two arguments. 
(1) A project name that will be used to create the environment variable.
(2) A path to where the project directory should be created at.
The project and path are used to create both an environment variable and value,
and a project name, path, and directory. 
The script will also change the working directory to the new project directory.
'''

import os
import sys
import argparse

# Try / Except to avoid key exception error
try:
    # Define argument parser and arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name')
    parser.add_argument('project_path')
    
    # parse arguments and set to usable variables
    args = parser.parse_args()
    project_name = args.project_name
    project_path = args.project_path

    #Function to make an env var from project name
    def make_ENV():
        #check if env var already exists
        if os.environ.get(project_name):
            print('Environment variable exists')
        #if none exists create one
        else:
            print('Environment variable does not exist...creating')
            os.environ[project_name] = project_path
            os.system('SETX {0} "{1}"'.format(str(project_name), str(project_path))) 
            os.system('export {0}'.format(str(project_name), str(project_path)))       
            print('Environment variable {} created'.format(project_name))
            print('{} set to {}'.format(project_name, project_path))
    
    # Function that makes/navigates a directory for project/ env var
    def make_DIR():
        # Check if dir exists, if not create one
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            print('Directory at {} created'.format(project_path))
            os.chdir(project_path)
            print('Navigating to directory')
        # If dir exists, navigate to it
        else:
            print('Directory already exists')
            print('Navigating to directory')
            os.chdir(project_path)
            os.system('cd {}'.format(str(project_path)))
            sys.path.append(project_path)
            print('Current working directory is: ' + os.getcwd())

    # Call functions
    make_ENV()
    make_DIR()
    
       
except KeyError:
    print('Define Environment Variable Manually')
    sys.exit(1)       






