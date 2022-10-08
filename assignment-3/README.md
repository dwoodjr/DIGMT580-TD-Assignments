# Assignment 3
In this repository is a collection of python scripts and a DOSKEY macros file. The scripts and macros allow the user to set a system wide environment variable with the name 'asset' through DOSKEY and create a new directory for that environment variable with a python script. The last python script will create a maya project(Ascii) and set an empty group with the same name asset.

## Repository

### Bin
Contains the directory with the generated maya file in it.

### Etc
Contains a macros.aliases file that has the DOSKEY commands for creating an environment variable and running MayaPy.
- macros.aliases

### Python
Contains two scripts for setting the environment variable value to a new directory and creating a maya file with an empty group called asset.
- setDir.py
- makeGrp.py

## HOW TO RUN (Windows)
To run the scripts navigate to a desired file directory.

Open a CMD terminal as administrator and load the macros with:
> DOSKEY /macros filename=macros.aliases
Run the DOSKEY command to create the environment variable
> DOSKEY casset

In the same directory as the python scripts run the two scripts as follows:
> python setDir.py
> MayaPy makeGrp.py
