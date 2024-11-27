#!/bin/bash

# Medium Fast modem bandwith is 250 kHz. 
# Frequencies are arranged in channels called "slots" and are directly adjacent to each other. 
# The center frequency of slot 1 is 902.125 MHz.
# The center frequency of slot 2 is 902.375 MHz.
# etc.

function measure_slot {
    slot=$1
    bandwidth_khz=$2
    average_over_seconds=$3
    measurement_duration_minutes=$4
    date=$(date +%Y%m%d%H%M%S)

    start_freq=$((902000 + (($slot - 1) * $bandwidth_khz)))
    end_freq=$(($start_freq + $bandwidth_khz))

    echo "Measuring slot $slot... (center frequency: $((($start_freq + $end_freq) / 2)) kHz)"
    rtl_power -f ${start_freq}k:${end_freq}k:250k -i ${average_over_seconds}s -e ${measurement_duration_minutes}m slot${slot}-$date.csv
}

# measure the noise floor for slots 17 through 23 (inclusive) with a bandwidth of 250 kHz,
# producing a datapoint every 10 seconds for 75 minutes
for slot in {17..23}; do
    measure_slot $slot 250 10 75
done