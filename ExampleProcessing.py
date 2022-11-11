######################
# Import Packages
######################
# Imports processing functions from separate files
from FuncOffline import process_plot

######################
# Set Paths
######################
# File paths in format "//"
file_location = "C://Users//simonha//PycharmProjects//BrainMirror//data//"
file_location_simon_pc = "C://Users//hanza//BrainMirror//data//"

######################
# Specify variables for the function
######################

# Exact names of datasets to analyse
analysed_datasets = [
    "211221_1_baseline",
    "211221_2_baseline"
]

# Names of channels for plots
channel_names = ["P7", "P8"]

# Save dataset name as
save_name = "BrainMirror_test_4"

######################
# Run Analysis
######################

process_plot(
             file_location=file_location_simon_pc,
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