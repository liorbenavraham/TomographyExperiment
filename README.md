# TomographyExperiment


random_bits.py

This Python script generates random bit vectors of varying lengths and prints them.

Description -
The script performs the following steps:
1. Generates three random bit vectors of lengths 10, 25, and 50.
2. Prints the generated bit vectors to the console.

Dependencies -
* numpy
* pandas

Example output -
10 bits: [0, 1, ...]
25 bits: [1, 0, ...]
50 bits: [0, 1, ...]

------------------------------------------------------

Simulation.py

This Python script simulates the detection of polarized light pulses in a quantum optics experiment. The simulation generates random bit sequences to represent light pulses and counts the coincident detections in different polarization states for varying numbers of bits.

Description -
The script performs the following steps:
1. Generates random bit sequences for a specified number of bits (500, 1000, and 2000).
2. Simulates the detection of polarized light pulses in two states: HHVV and HVVH.
3. Records the detection counts for vertically (V) and horizontally (H) polarized light for each state.
4. Calculates and prints the detection probabilities for each state and number of bits.

Dependencies -
* numpy


Example output -
num of bits: 1000
state: HHVV: V count = 503
state: HHVV: H count = 497
Probabilities (V,H): (0.503,0.497)

num of bits: 1000
state: HVVH: V count = 479
state: HVVH: H count = 521
Probabilities (V,H): (0.479,0.521)

------------------------------------------------------

Bell.py

This Python script simulates the detection of polarized light pulses in a quantum optics experiment. The simulation generates random bit sequences to represent light pulses and counts the coincident detections in different polarization states for varying numbers of bits.

Description -
The script performs the following steps:
1. Reads data from an Excel file containing simultaneous recordings from two cameras.
2. Identifies intensity values above a specified threshold and counts the correlations between the two cameras for various angles.
3. Calculates the E parameters and subsequently the S parameter.
4. Computes the uncertainty in the S parameter using the partial derivatives and the square root of the counts.

Dependencies -
* numpy
* pandas

Example output -
S: 2.335
Delta S: 0.284

------------------------------------------------------

Final3DPlotterSaraGarry.m

This MATLAB script reads data from a CSV file, processes it, and generates a 3D bar plot. The script also saves the figure as both a .fig file and a .png image.

Description -
The script performs the following steps:
1. Extracts the base name and bit number from the filename.
2. Reads a data matrix from a CSV file and normalizes it based on the bit number.
3. Creates a 3D bar plot of the data.
4. Sets axis labels, titles, and other plot aesthetics.
5. Saves the figure as both a .fig file and a .png image.

Usage -
1. Ensure your data file (e.g., HHVV10.csv) is placed in the same directory as the script.
2. Run the script in MATLAB to generate and save the plot.

------------------------------------------------------

Plot_Intensity_PartA.m

This MATLAB script is based on the given plotter_gary.m script. It reads a video file, processes each frame to calculate the sum of pixel intensities in specified regions, and plots the intensity over time.

Description -
The script performs the following steps:
1. Reads a video file.
2. Iterates through each frame to calculate the sum of pixel intensities in specified regions of interest.
3. Plots the intensity values over the frames.

Usage -
1. Ensure your video file (e.g., partA_50.mp4) is placed in the same directory as the script.
2. Update the regions of interest (coordinates) as needed.
3. Run the script in MATLAB to generate the plot of intensity values over frames.

------------------------------------------------------

Plot_Intensity_PartB.m

This MATLAB script is also based on the given plotter_gary.m script. It reads a video file, processes each frame to calculate the sum of pixel intensities in specified regions, and plots the intensity over time for two cameras (Alice and Bob).

Description -
The script performs the following steps:
1. Reads a video file.
2. Iterates through each frame to calculate the sum of pixel intensities in specified regions of interest for Alice and Bob.
3. Plots the intensity values for both Alice and Bob over the frames.

Usage -
1. Ensure your video file (e.g., partA_50.mp4) is placed in the same directory as the script.
2. Update the regions of interest (coordinates) as needed.
3. Run the script in MATLAB to generate the plot of intensity values over frames for both cameras.