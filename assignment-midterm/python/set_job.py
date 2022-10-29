import os
import sys
import argparse

'''
Set project directory and project env to specified path
'''
parser = argparse.ArgumentParser()
parser.add_argument('job', help='enter project path')
args = parser.parse_args()

def setJOB():
    os.environ['JOB'] = args.job
    os.environ['HIP'] = args.job

def loadDoskey():
    os.system('cmd /c DOSKEY /macrofile=/bin/.aliases')
    os.system('"E:/Side Effects Software/Houdini 19.5.368/bin/hcmd.exe"')
def runDoskey():
    os.system('cmd /c hcmd')
    
loadDoskey()
runDoskey()
setJOB()