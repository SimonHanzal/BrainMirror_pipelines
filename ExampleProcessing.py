######################
# Import Packages
######################
# Imports processing functions from separate files
from FuncOffline import process_plot
# And numpy to get the peak values
import numpy as np
import pandas as pd
######################
# Set Paths
######################
# File paths in format "//"
file_location = "C://Users//simonha//PycharmProjects//BrainMirror//data//"
file_location = "C://Users//simonha//OneDrive - University of Glasgow//neurofeedback_pilot_2022-23//piloting//"


print()

######################
# Specify variables for the function
######################

# Exact names of datasets to analyse
"""
analysed_datasets = [
    "2111011_1_baseline",
    "2211012_1_baseline",
    "2211021_1_baseline",
    "2311012_1_baseline",
    "2311021_1_baseline",
    "2311031_1_baseline",
    "2811011_1_baseline",
    "2811022_1_baseline",
    "2911012_1_baseline",
    "3011011_1_baseline",
    "3011032_1_baseline",
    "3011052_1_baseline",
    "612011_1_baseline",
    "1212011_1_baseline",
    "1212022_1_baseline",
    "1212031_1_baseline",
    "1212041_1_baseline",
    "1212052_1_baseline",
    "1212062_1_baseline",
    "1312011_1_baseline",
    "1312022_1_baseline",
    "1312032_1_baseline",
    "1312041_1_baseline",
    "1712012_1_baseline",
    "1912011_1_baseline"
]

analysed_datasets = [
    "2111011_2_baseline",
    "2211012_2_baseline",
    "2211021_2_baseline",
   # "2311012_2_baseline",
    "2311021_2_baseline",
    "2311031_2_baseline",
    "2811011_2_baseline",
    "2811022_2_baseline",
    "2911012_2_baseline",
    "3011011_2_baseline",
    "3011032_2_baseline",
    "3011052_2_baseline",
    "612011_2_baseline",
    "1212011_2_baseline",
    "1212022_2_baseline",
    "1212031_2_baseline",
    "1212041_2_baseline",
    "1212052_2_baseline",
    "1212062_2_baseline",
    "1312011_2_baseline",
    "1312022_2_baseline",
    "1312032_2_baseline",
    "1312041_2_baseline",
    "1712012_2_baseline",
    "1912011_2_baseline"
]

analysed_datasets = [
    "2111011_3_mirror",
    "2211012_3_mirror",
    "2211021_3_mirror",
    "2311012_3_mirror",
    "2311021_3_mirror",
    "2311031_3_mirror",
    "2811011_3_mirror",
    "2811022_3_mirror",
    "2911012_3_mirror",
    "3011011_3_mirror",
    "3011032_3_mirror",
    "3011052_3_mirror",
    "612011_3_mirror",
    "1212011_3_mirror",
    "1212022_3_mirror",
    "1212031_3_mirror",
    "1212041_3_mirror",
    "1212052_3_mirror",
    "1212062_3_mirror",
    "1312011_3_mirror",
    "1312022_3_mirror",
    "1312032_3_mirror",
    "1312041_3_mirror",
    "1712012_3_mirror",
    "1912011_3_mirror"
]
"""
analysed_datasets = [
    "2111011_4_mirror",
    "2211012_4_mirror",
    "2211021_4_mirror",
    "2311012_4_mirror",
    "2311021_4_mirror",
    "2311031_4_mirror",
    "2811011_4_mirror",
    "2811022_4_mirror",
    "2911012_4_mirror",
    "3011011_4_mirror",
    "3011032_4_mirror",
    "3011052_4_mirror",
    "612011_4_mirror",
    "1212011_4_mirror",
    "1212022_4_mirror",
    "1212031_4_mirror",
    "1212041_4_mirror",
    "1212052_4_mirror",
    "1212062_4_mirror",
    "1312011_4_mirror",
    "1312022_4_mirror",
    "1312032_4_mirror",
    "1312041_4_mirror",
    "1712012_4_mirror",
    "1912011_4_mirror"
]
# Names of channels for plots
channel_names = ["P7", "P8"]

# Save dataset name as
#save_name = "Beginning_values"
save_name = "sham_middle_power"

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
             convert_mean=False,
             convert_max=False
)
#Converted to power and demeaned.

######################
# Load, arrange and export data
######################

# Loop through the exported datasets
max_values_1 = np.zeros(len(analysed_datasets))
max_values_2 = np.zeros(len(analysed_datasets))
max_index_1 = np.zeros(len(analysed_datasets))
max_index_2 = np.zeros(len(analysed_datasets))

i = []
for i in range(len(analysed_datasets)):
    data = np.genfromtxt("data/" + analysed_datasets[i] + "_output.csv", delimiter=" ")
    max_values_1[i] = np.max(data[933:1399, 1])
    temp = int(np.argmax(data[933:1399, 1]))
    max_index_1[i] = data[932+temp, 0]

for i in range(len(analysed_datasets)):
    data = np.genfromtxt("data/" + analysed_datasets[i] + "_output.csv", delimiter=" ")
    max_values_2[i] = np.max(data[933:1399, 2])
    temp = int(np.argmax(data[933:1399, 2]))
    max_index_2[i] = data[932+temp, 0]

df = pd.DataFrame({'Participant':analysed_datasets, 'P7':max_values_1, 'P8':max_values_2})
df2 = pd.DataFrame({'Participant':analysed_datasets, 'P7':max_index_1, 'P8':max_index_2})

df.to_csv(path_or_buf="data/sham_middle_power.csv", sep=',')
df2.to_csv(path_or_buf="data/sham_middle_power_peaks.csv", sep=',')
#df.to_csv(path_or_buf="data/end_channel.csv", sep=',')


# 2. Extract first 1 - 59 628 = first three minutes - change in the FuncOffline code
# 3. Extract last  139 132 to 198 760  - change in the FuncOffline code
# 4. Filter? l_freq=8 change to =4 or even lower to look at different segments
