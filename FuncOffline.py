# Packages used
import matplotlib
# Used to surpress an issue in matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
# Used to surpress an issue in pandas
pd.set_option('mode.chained_assignment',None)
from control import mag2db as db
from math import isnan
from mne.filter import filter_data as mne_filter
from scipy.fft import fft
from scipy.signal import savgol_filter
from scipy.signal import detrend, welch
from scipy.signal.windows import hann
from statistics import mean

def software_import(file_location, dataset, software):
    # Which can either be the original BioTrace .txt export file.
    if software == "biotrace":
        file_path = os.path.abspath(
            file_location + dataset + ".txt")
        data = pd.read_csv(file_path, header=None)
        return np.array(data.iloc[:, 1:2])
    # Or the CSV produced by brainmirror.
    elif software == "brainmirror":
        data = np.genfromtxt(os.path.abspath(file_location +
                                             dataset + ".csv"), delimiter=',')
        return np.array(data[1:, 0:2])
    else:
        print("Software must be either 'biotrace' or 'brainmirror'.")


def substitute_errors(data, mean_value):
    # Replacing 0 and NA values based on mean, of course only if there's something to base the mean on.
    if not isnan(mean_value):
        for i in range(len(data - 1)):
            if data[i] == 0 or isnan(data[i]):
                data[i] = mean_value
    return data


def analyse_all(dataset, software, SRATE, convert_power=True, convert_decibels=False, convert_mean=True, convert_max=True):
    # And every channel
    data = software_import(file_location, dataset, software)
    all_frequencies = np.empty([int(len(data[:, 0])/2), 2])
    all_PS = np.empty([int(len(data[:, 0])/2), 2])
    for k in range(2):
        # 1. Preparing Data
        channel_calculation = data[:, k]
        channel_mean = mean(channel_calculation)

        # 2. Patching up Data
        channel_calculation = substitute_errors(channel_calculation, channel_mean)
        # Converting data into a workable array
        channel_calculation = np.array(channel_calculation)

        # 3. Detrending data
        channel_calculation = detrend(channel_calculation)

        # 4. Filtering
        # Applying a MNE-based 8-30Hz firwin filter:
        # A Hamming window with 0.0194 passband ripple and 53 dB stopband attenuation
        channel_calculation = mne_filter(channel_calculation, sfreq=SRATE, l_freq=8, h_freq=30, method="fir")
        # A useful feature is to save the data at this stage when it is somewhat preprocessed
        #  np.savetxt("test.txt", simulated_raw)

        # 5. FFT
        # Applying a FFT
        freq_data = fft(channel_calculation)
        # a possible alternative:
        # freq_data, something = welch(simulated_raw, frequencies, window=hann(1024, True),
        # noverlap=128, nfft=1024, return_onesided=True)
        # Getting the total number of channels, necessary for the calculation

        # 6. Getting the Frequencies
        number = len(channel_calculation)
        frequencies = np.linspace(0, SRATE/2, int(number / 2))
        # The y axis time frequency data, refined based on the number of observations

        # 7. Using only useful data.
        # Using the absolute value of the fourier transform and only showing the first half.
        channel_calculation = (2 / number * np.abs(freq_data[0: int((number / 2))]))

        # 8. Standardising the data for display
        # Converting amplitudes to power
        if convert_mean:
            power_mean = np.mean(channel_calculation)
            #            if type(amplitude_max) == 'float':
            channel_calculation = channel_calculation / power_mean
        if convert_power:
            channel_calculation = channel_calculation ** 2
        # Converting data to decibels
        if convert_decibels:
            channel_calculation = db(channel_calculation)
        # De-meaning (should check that it is a number)
        # Baseline-correcting
        if convert_max:
            power_max = np.max(channel_calculation)
            #           if type(amplitude_max) == 'float':
            channel_calculation = channel_calculation/power_max

        # 9. Smoothing: applying a savgol filter with a generous window size of 499 and polynomial order of 2
        channel_calculation = savgol_filter(channel_calculation, 499, 2)

        # 10. Saving at the end
        all_frequencies[:, k] = frequencies
        all_PS[:, k] = channel_calculation
    return all_frequencies, all_PS


def process_plot(file_location, dataset, name, software, SRATE, channel_names,
                 convert_power=True, convert_decibels=True, convert_mean=True, convert_max=True):
    # Colour map
    cmap = matplotlib.cm.get_cmap('gist_rainbow')
    plot_colour = np.linspace(0, 1, 5)
    # Initialise
    matplotlib.use('TkAgg')
    plt.figure(figsize=(24, 16))
    plt.ion()
    # For every participant
    for i in range(len(dataset)):
        frequencies, power_db = analyse_all(file_location, dataset[i], software, SRATE, convert_power,
                                            convert_decibels, convert_mean, convert_max)
        for k in range(2):
            plt.subplot(1, 2, k+1)
            plt.title(channel_names[k])
            plt.xlabel('Frequency in Hz')
            plt.ylabel('Power')
            plt.xlim([2, 40])
            plt.plot(frequencies[:, k], power_db[:, k], color=cmap(plot_colour[i]), alpha=0.55)
    # Just showing the first 40 Hz
    #  plt.ylim([0.3, 1])
    plt.draw()
    plt.show()
    plt.savefig('plots/offline_plots/'+name+'.png')
    plt.close()
