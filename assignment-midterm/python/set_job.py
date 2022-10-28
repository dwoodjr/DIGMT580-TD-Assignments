import hou
import os
import argparse

'''
Set project directory and project env to specified path
'''
parser = argparse.ArgumentParser()
parser.add_argument('job', help='set project path')
args = parser.parse_args()

def setJOB():
    os.environ['JOB'] = args.job
    os.environ['HIP'] = args.job
