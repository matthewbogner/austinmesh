#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
#data = pd.read_csv('location/MRBh/output.csv', header=None, names=['date', 'time', 'startFreq', 'stopFreq', 'stepSize', 'numSamples', 'power'])
data = pd.read_csv('location/MRBh/output.csv', header=None, names=None)

# The CSV file does not contain column headers in the first row.  Read the first row to determine how many power measurement bins there are.
with open('location/MRBh/output.csv', 'r') as f:
    first_line = f.readline().strip()
    start_freq_hz = first_line.split(',')[2]
    stop_freq_hz = first_line.split(',')[3]
    step_size_hz = first_line.split(',')[4]
    num_bins = len(first_line.split(',')) - 6



# Plot the data
plt.figure(figsize=(10, 6))
for freq in data['frequency'].unique():
    subset = data[data['frequency'] == freq]
    plt.plot(subset['timestamp'], subset['power'], label=f'{freq} Hz')

plt.xlabel('Time')
plt.ylabel('Power (dB)')
plt.title('Noise Floor Over Time')
plt.legend()
plt.show()