%% 0. Setup %%

%% 1. Data Wrangling %%

clear all


data = table2array(readtable('C:\Users\simonha\PycharmProjects\BrainMirror\data\20102401_2_baseline.csv'));
% data = table2array(data);
save('20102401_2_baseline.mat', 'data');

%% 2. Opening Data in EEGLab %%


eegLabPath                      = 'C:\Users\simonha\AppData\Roaming\MathWorks\MATLAB Add-Ons\Collections\EEGLAB';
addpath(eegLabPath)
[ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
eeglab redraw;

%% 3. Preprocessing Data %%

% Removing bad data %

% Detrending %

% Filtering %

% Epoching % #optional

% Exporting %

%% 4. Time-Frequency Analysis %% <- Cohen course on FFT

cd("C:\Users\simonha\PycharmProjects\BrainMirror_pipelines")
data = table2array(readtable('test.txt'));

fs=512;
x=data;
N=length(x);
ts=1/fs;
tmax=(N-1)*ts;
t=0:ts:tmax;
plot(t,x);  % plot time domain

nfft = 2^( nextpow2(length(x)) );
df = fs/nfft;
f = 0:df:fs/2;
X = fft(x,nfft);
X = X(1:nfft/2+1);
figure; plot(f,sqrt(abs(X))); axis([0,50,0,10e2])

% Smoothing %

% Extracting value

[value where] = max(f(1000:end))
