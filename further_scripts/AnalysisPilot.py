from FuncOffline import process_plot
from FuncWelchOffline import process_plot_welch

#####################
# Participant names #
#####################
# Summer Research data
# participants_exp = ["e_01", "e_02", "e_03", "e_04", "e_05", "e_06", "e_07", "e_08", "e_09", "e_10", "e_11", "e_12"]
# participants_control = ["c_01", "c_02", "c_04", "c_09"] #"c_03", c_05, "c_06", "c_07" and  "c_08" causing errors
# Early Piloting data

# test_1910 = ["19012201_10_baseline", "19012201_11_baseline", "20102401_1_baseline",
# "20102401_2_baseline", "20102401_5_mirror"]

file_location = "C://Users//simonha//PycharmProjects//BrainMirror//data//"
file_location_simon_pc = "C://Users//hanza//BrainMirror//data//"
test_0410 = ["211221_1_baseline", "211221_2_baseline"]
channel_names = ["PO7", "PO8"]
save_vanilla_as = "BrainMirror_test_4"
save_welch_as = "BrainMirror_test_3"

process_plot(file_location_simon_pc, test_0410, save_vanilla_as, "brainmirror", 512, channel_names,
             convert_max=False, convert_decibels=False)

# process_plot_welch(file_location, test_0410, save_welch_as, "brainmirror", 512, channel_names,
#              convert_mean=False, convert_power=False, convert_max=False, convert_decibels=False)