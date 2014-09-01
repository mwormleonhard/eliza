#Project ELIZA
A wellplate reader implemented in python and openCV.

##Current version / state
0.1 / Basic functionality done. Probably not robust / stable


## Objectives
###Minimum
The finished script/program should take a top-down picture of a wellplate as input and be able to report mean RGB values for each well to a flat CSV textfile or equivalent.

###Options / Wishes / Ideas
* Interactive as well as autonomous mode, automatically optimising parameters for feature identification.
* Calulation of color excess function
* (Limited) Data analysis features - automatic calibration and calculation of concentrations based on a selected signal.

## Status / TODO
###HW
* Try to make a paper mask for wellplates or coloring the flat parts. Should make circle detection much easier.
* Experiment with illumination

####DONE
* Coloring well rims with sharpie: Very robust detection.
 
###SW
* Make circle detection robust (See HW)

####DONE
* Construct function for basic output functionality
* Interactive window for playing with parameters
* Outputs overlaid image for demonstration / testing
