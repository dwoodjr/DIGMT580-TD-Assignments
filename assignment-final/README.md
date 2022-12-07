# FINAL

In this repository is a collection of scripts and files needed to run/test two tools. The first tool is a Houdini Digital Asset (HDA) that processes geometry point data (from still geometry or a cached simulation) into midi note data that can be used to play sounds in the Digital Audio Workstation (DAW) Reaper. The second tool is a Reaper Action script with GUI (written in Lua) that automates the setup of tracks, midi channels, and track FX to the specified number of tracks. These tracks correspond to the maximum number of Midi channels defined in the HDA.

This repository requires the user have both SideFX Houdini and the Houdini Music Toolset (HMT) plugin installed. As well as Reaper with the midi devices and midi data routing properly setup. The geometry that can be processed by the scripts has only been tested with Houdini standard geometry and simulation formats (.geo adn .bgeo.sc).

## Repository

### Bin

Contains two folders that house the HDA and Lua scripts.

- hda
  - sop_note_processor.2.0.hdanc
    - This is a binary file that houses the Houdini Digital Asset. *There are other incomplete assets as well*.
  - test_scene.hipc
    - This is a Houdini file that can be used to run the HDA
- reaper
  - create_tracks.lua
    - This is the script used to run the track creation automation in Reaper.
  - midi_tracks.rpp
    - This is a Reaper file that can be used to run the tools.

### Etc

Contains a folder that houses a cached simulation that can be used with the HDA.

- geo
  - test_scene.sim_v1.(0001-0240).bgeo.sc
    - The cached point simulation frames 1-240

### Python

Contains scripts for setting the houdini project and environment variables, processing geometry, setting up a houdini scene, and exporting to a hip file.

- notes.py
  - This script is a copy of the python code that is used by the HDA to process point data into midi data.


## HOW TO RUN (Windows)

To run the scripts do the following.

1. Open the Houdini test scene and load in the HDA file. Adjust the parameters as desired.
Make sure to place the HDA into a SOP level geometry node.
The timeline in Houdini needs to be set to real-time playback.
In the HDA  any parameter with a Maximum and Minimum can be randomized. Use the same values in both fields for constant.

- Select the simulation with the "simulation files" parameter.
- Set teh starting note with "Starting Note" (integer between 0 - 127)
- Set the "Note Offset" (float between 0 - 10)
- Set the "Note Duration" Maximum and Minimum (float 0 - 10)
- Set the "Note Velocity" Maximum and Minimum (float 0 - 1)
- Set the "Number of Channels" Maximum and Minimum (integer 1 - 16)

> test_scene.hipc
> sop_note_processor.2.0.hdanc

2. Open the Reaper test file and load in the action script.
On the top toolbar go to *Actions* > *New action* > *Load ReaScript...*.
Then navigate to the .lua script and hit *Start*

- In the user prompt section enter the same number as the "Maximum Number of Channels" from HDA.

> midi_tracks.rpp
> create_tracks.lua

3. To hear the simulation both Houdini and Reaper need to be open at the same time. After setup of HDA and midi tracks, go back to Houdini and press play on the timeline.

- The Reaper action script should default to the "ReaSynth" VST that is included with reaper. If a differetn sound is desired, all track FX chains will need to be manually edited with the desired FX.
