# MIDTERM

In this repository is a collection of scripts and files needed to run the command-line tool that processes geometry point data into midi note data that can be used to play sounds in a DAW.
This repository requires the user have both SideFX Houdini and the Houdini Music Toolset (HMT) plugin installed. The geometry that can be processed by the scripts must be in .geo or .bgeo formats (Houdini standard geometry formats). The python script that generates the midi note point data need to be run in Houdini Command-line (hcmd).

## Repository

### Bin

Contains a DOSKEY macros file.

- .aliases
  - This file contains the DOSKEY macro definition to run the hcmd command. The Houdini hcmd.exe path can be changed to match the user's system.

### Python

Contains scripts for setting the houdini project and environment variables, processing geometry, setting up a houdini scene, and exporting to a hip file.

- hou_setup.py
  - This script contains system variable checks and other code to run Houdini in command-line
- set_job.py
  - This script loads and runs the hcmd DOSKEY. It also sets the HIP and JOB variables to the desired project path.
- gen_hmt.py
  - This script is responsible for generating the node network needed to create midi note data
- pt_parm.txt
  - This file contains the python code that is imported into the Python SOP node in the gen_hmt.py script.

### Etc

- hmtNotes.hipc
  - This is an example of a generated Houdini file with node network and midi note data.
- test.bgeo
  - This is a test geometry file that is processed by python scripts.

## HOW TO RUN (Windows)

To run the scripts do the following.

1. Open a CMD terminal as administrator and run the setup script.
Make sure to pass in the following arguments: Project Path
This script will create a hcmd environment in the terminal. The rest of the scripts must be run in hcmd.

> python set_job.py args*

2. In the same terminal (it should now be in a hcmd environment) run the midi note processing script.
Make sure to pass in the following arguments: Project Path, Geometry Asset Path (.bgeo file), Midi Note Starting Value (integer between 0 - 127)

> python gen_hmt.py args*
