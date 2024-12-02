#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os
import numpy

def moving_average(data, window_size):
    return numpy.convolve(data, numpy.ones(window_size) / window_size, mode='valid')

def analyze_channel(csv_file: str) -> None:
    data = pd.read_csv(csv_file, header=None, names=['date', 'time', 'startFreq', 'stopFreq', 'stepSize', 'numSamples', 'power1', 'power2', 'power3'])
    freq = data['startFreq'][0]
    subset = data[data['startFreq'] == freq]
    center_freq_mhz = (freq + 125000) / 1000000
    smoothed_measures = moving_average(subset['power1'], 12) # 12 smooths across 2 minutes
    # Adjust the time axis to match the length of the smoothed data
    smoothed_time = subset['time'][len(subset['time']) - len(smoothed_measures):]
    plt.plot(smoothed_time, smoothed_measures, label=f'{center_freq_mhz} MHz')

def analyze_all_channels(location_dir: str) -> None:
    # Get only the CSV files in the location_dir that start with 'slot' and end with '.csv'
    csv_files = [f'{location_dir}/{fn}' for fn in os.listdir(location_dir) if fn.startswith('slot') and fn.endswith('.csv')]
    # sort the files by the date in the filename
    csv_files.sort(key=lambda x: x.split('-')[1])
    for csv_file in csv_files:
        print("Processing", csv_file)
        analyze_channel(csv_file)

def save_results_graph(location: str, location_dir: str) -> None:
    plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=30))  # Limit the number of ticks on the X-axis
    plt.xlabel('Time')
    plt.ylabel('Power (dB)')
    plt.title(f'{location} Noise Floor Over Time')
    plt.legend()
    plt.savefig(f'{location_dir}/{location}-results.png')
    plt.close()

locations = [location for location in os.listdir('location') if os.path.isdir(f'location/{location}')]
for location in locations:
    location_dir = f'location/{location}'
    plt.figure(figsize=(10, 10))
    analyze_all_channels(location_dir)
    save_results_graph(location, location_dir)
