# Assignment 4
In this repository is a collection of python scripts and maya files. The first script allows the user to set a system wide environment variable/ project name and create a new directory by passing in arguments. The second python script will create save a maya project(Ascii) that has a set naming convention and increments the file version number.

## Repository

### Bin
Contains the directory with the generated maya files in it.

### Python
Contains two scripts for setting the environment variable value to a new directory and creating a maya file with incrementing version numbers.
- setDir.py
- saveAsset.py

## HOW TO RUN (Windows)
To run the scripts navigate to the scripts location.

Open a CMD terminal as administrator and run the setup script.
Make sure to pass in the following arguments: Project Name, Project Path
> python setDir.py args*

Close the first terminal and open a new one. Run the save file script in a MayaPy environment.
Make sure to pass in the following arguments: Asset Name, Asset Type, Artist Name, Version Number
> mayapy saveAsset.py args*
