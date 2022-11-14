# Assignment 5

In this repository is a collection of scripts and files needed to run the command-line file setup and PyQt Maya widget.
This repository requires the user to be running a Windows OS and to be load/run the UI scripts in the Maya project Script Editor.

## Repository

### Bin

Contains a Maya .ma file.

- cubeUI.ma
  - This file contains nothing. It is an empty maya ascii project that is created when the open.py script is run.

### Python

Contains scripts for setting the Maya project and environment variables, creating/saving a project, opening the Maya file.

- mayaUI.py
  - This script contains the code required to run the Make-a-Cube maya plugin (Python Version). It must be run in the Maya Script Editor.
- open.py
  - This script creates, saves, and loads up the cubeUI.ma Maya project file.
- pyMayaGUI.py
  - This script contains the code required to run the Make-a-Cubes maya plugin (PyQt Version). It must be run in the Maya Script Editor.
- setDir.py
  - This file contains code needed to set the project directory and environment variables for the Maya project.

### Etc

- Empty Directory

### UI

- Empty Directory

## HOW TO RUN (Windows)

To run the scripts do the following.

1. Open a CMD terminal as administrator and run the setup scripts.
Make sure to pass in the following arguments: Project Path
The second script will launch Maya. The remainder of the scripts are run in Maya Script Editor.

> python setDir.py args*

> python open.py

2. In the Maya Script Editor load the python scripts (file->open script->navigate to script location).
Both scripts do the same thing, create a specified number of cubes with specified dimensions.
One script is traditional Maya Python, the other is a PySide Qt Widget version.

> mayaUI.py

> pyMayaGUI.py
