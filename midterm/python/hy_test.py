def enableHouModule():
    '''Set up the environment so that "import hou" works.'''
    import sys, os
    
    if hasattr(sys, "setdlopenflags"):
        old_dlopen_flags = sys.getdlopenflags()
        sys.setdlopenflags(old_dlopen_flags | os.RTLD_GLOBAL)

    if sys.platform == "win32" and hasattr(os, "add_dll_directory"):
        os.add_dll_directory("{}/bin".format(os.environ["HFS"]))

    try:
        import hou
    except ImportError:
        sys.path.append(os.environ['HHP'])
        import hou
    finally:
        if hasattr(sys, "setdlopenflags"):
            sys.setdlopenflags(old_dlopen_flags)
            
enableHouModule()


import hou
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('job', help='path to the project directory')
parser.add_argument('geo', help='path to the .bgeo geometry object')
args = parser.parse_args()


OBJ = hou.node('/obj')
geo = OBJ.createNode('geo')
file = geo.createNode('file')
file.parm('file').set(args.geo)

hou.hipFile.save(file_name = '{}/test.hipc'.format(args.job))