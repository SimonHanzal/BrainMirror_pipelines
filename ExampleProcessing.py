######################
# Import Packages
######################
# Imports processing functions from separate files
from FuncOffline import process_plot
# And numpy to get the peak values
import numpy as np
######################
# Set Paths
######################
# File paths in format "//"
file_location = "C://Users//simonha//PycharmProjects//BrainMirror//data//"
file_location_simon_pc = "C://Users//hanza//BrainMirror//data//"
save_to = "C://Users//hanza//BrainMirror//data//"

######################
# Specify variables for the function
######################

# Exact names of datasets to analyse
analysed_datasets = [
  #  "211221_1_baseline",
  #  "211221_2_baseline",
  #  "2810221_1_baseline",
  #  "2810221_2_baseline",
  #  "19012201_10_baseline",
  #  "19012201_10_baseline",
  #  "20102201_2_baseline",
  #  "20102201_1_baseline",
  #  "20102401_1_baseline",
  #  "20102401_2_baseline",
    "9111_1_baseline",
    "9111_2_baseline",
    "161122_1_baseline",
    "161122_2_baseline"
]

# Names of channels for plots
channel_names = ["P7", "P8"]

# Save dataset name as
save_name = "BrainMirror_test_17112"

######################
# Run Analysis
######################

# We will modify the function to specify what time window
process_plot(
             file_location=file_location,
             dataset=analysed_datasets,
             name=save_name,
             software="brainmirror",
             SRATE=512,
             channel_names=channel_names,
             # These arguments can be played with
             convert_power=True,
             convert_decibels=False,
             convert_mean=True,
             convert_max=False
)

######################
# Load, arrange and export data
######################

# Loop through the exported datasets

data = np.genfromtxt("data/" + analysed_datasets[0] + "_output.csv", delimiter=" ")
pass
    # Select relevant values

# Add them to a final dataframe

# Save dataframe for loading into R

#
