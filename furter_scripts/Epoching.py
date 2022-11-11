# TODO: Systematically go through Lucie's data.
#  This packages is necessary for EEG data processing
import mne
# This packages is necessary for arrays.
import numpy as np
#  Needed to get the paths working
import os
# Some transformations are done in data frames.
import pandas as pd
# This is just for corrections.
import matplotlib as mpl
# This is the command needed for bugfixing to work in PyCharm.
mpl.use('TKAgg')
from FuncOffline import substitute_errors
from statistics import mean
# Here, an mne info object is generated to fit the txt data from BrainMirror or BioTrace recordings.
# There are 2, timestamps need to be dealt with before and the data needs to be sent in chunks to avoid extra computing.
# TODO: 2 Look at timestamp-time mismatch.
n_channels = 2
# These are O1 and O2 only for now.
# TODO: 1 Put in place holders for two electrodes and store local information in a different way.
ch_names = ['O1']+['O2']
# This is a very stable command.
ch_types = ['eeg'] * 2
# This is 256 for BioTrace, 512 for BrainMirror
sampling_freq = 256
# info created here
info = mne.create_info(ch_names, sfreq=sampling_freq, ch_types=ch_types)
info.set_montage('standard_1020')
info['description'] = 'E_02'
# Use this command for CSVs.
# data = np.genfromtxt('data//e_02_easy.txt', delimiter=',')
# Otherwise this is used for TXT files. Max_rows needs to be played with, but last rows are causing issues.
# TODO: Implement a checker that data is cleaned so that max_rows is not needed.
# TODO: Clip the data a bit and compare it with Lucie's notes.
data = np.loadtxt(os.path.abspath('C://Users//simonha//PycharmProjects//BrainMirror//data//external_software//e_09.txt'), delimiter=',', max_rows=800000)
"""
# This is where dataframes come in to remove rows, this could probably be done more elegantly.
# TODO: Redo offline data wrangling to be more elegant.
# TODO: Figure out similarity between BioTrace and BrainMirror.
data = pd.DataFrame(data, columns=['time', 'O1', '02'])
data = data.drop_duplicates(subset=['time'])
# Data wanted in rows for some reason.
data = data.transpose()
data = data.to_numpy(na_value=0)
data = np.delete(data, [1], axis=0)
"""
# This bit is a nightmare as the scales is often really mismatched on BrainMirror for some bizzare reason.
# TODO: Figure out what is going on with scaling issues.
# data *= 1e-07
data = data[:,1:2]
for i in range(1):
    channel_mean = mean(data[:, i], )
    data[:, i] = substitute_errors(data[:, i], channel_mean)

# TODO: Try the filtering process on data which should be ok, to see what comes out.
# This filtering process copies that which is used in NFBLab by default, first a 4th order Butterworth filter.
simulated_raw = mne.filter.filter_data(data, sfreq=256, l_freq=3, h_freq=30, method="iir")
# Followed by composing the mne object
simulated_raw = mne.io.RawArray(simulated_raw, info)
# And then applying a Savitzky–Golay smoothing of the 2nd order
simulated_raw = simulated_raw.savgol_filter(h_freq=30)
# Generating second-long events,
fake_events = np.zeros((3000, 3))
for i in range(1, 3000):
    fake_events[i, 0] = i*256
# saving them,
np.savetxt("fake_events_eve.txt", fake_events)
# loading them
events = mne.read_events("fake_events_eve.txt")
# and changing event markers.
events[:, 2] = 1
# This applies the events to the mne object.
new_events = mne.make_fixed_length_events(simulated_raw, start=0, stop=4000, duration=1)
# This dds epochs based on events.
simulated_epochs = mne.Epochs(simulated_raw, events=events)
pass
# These are the two options for plotting, either time or time-frequency.
# simulated_epochs.plot(show_scrollbars=False, picks="O2") #picks='eeg',
# Currently really works just on one channel at the time as the two are so disproportional
simulated_epochs.plot_psd(fmin=3., fmax=30., average=True, spatial_colors=False, picks="O2", dB=True)
#This command is used for bugfixing.
pass