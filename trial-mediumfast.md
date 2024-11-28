# Trialing MediumFast in Austin, TX

## Overview

This is a proposal for testing the [Meshtastic](https://meshtastic.org) MediumFast modem preset in the Austin metro area, in coordination with the broader community at [AustinMesh](https://www.austinmesh.org).

## Goal

Test the efficacy of MediumFast in the Austin metro area, by measuring the impact of MediumFast on channel utilization and mesh reliability.

## Why

As the mesh grows in Austin, so does channel utilization.  Channel utilization is an [influencing metric in the firmware](https://github.com/meshtastic/firmware/blob/master/src/airtime.h#L49) for deciding how often various modules are allowed to send data via LoRa, or whether it is sent [at all](https://github.com/meshtastic/firmware/blob/master/src/airtime.cpp#L123).

There are many ways to help manage the growth of channel utilization.  One way is to encourage best practices with setting things like maximum hops and reporting intervals for the various modules.  Another way, is to use a different modem preset, such as MediumFast, which has a faster data rate.  Faster data rates means a node spends less time transmitting.

The Austin mesh is not yet exceeding the 40% max channel utilization, and very infrequently spikes above 25%.  See [Bridger graph of channel utilization](https://graphs.austinmesh.org/d/ddpwwgtdxf2m8f/austin-mesh?orgId=1&viewPanel=13&from=now-30d&to=now).  The purpose of this trial is not to suggest making an immediate switch of modem presets or frequencies, but to gather data and lessons learned for when/if that day eventually comes.

## Guiding Principles

1. ***Minimize disruption***: Do our best to not disturb our currently functioning mesh.  We have new nodes joining the mesh successfully on a regular basis, and we should do our best to avoid creating a poor onboarding experience for our new friends.
1. ***Data driven***: Collect copious quantities of data.  Let the data guide the experiment.  Any future decisions to switch frequencies and/or modem presets away from defaults will be met with justifiable skepticism - the data should be recorded durably so that it remains available in high fidelity for future mesh participants.
1. ***Be open-minded***: Allow your previously held assumptions to be challenged.  This is a learning exercise, be patient.

## How the test will be conducted

These steps are listed in order.

1. Identify key nodes in the Austin area
    - Recommend choosing the top X nodes with the highest AirUtil % as reported to Bridger -- objectively, these are the nodes carrying the bulk of the traffic.
1. Identify candidate frequency slots that will be on the short list for consideration
    - Maximize our ability to use existing spare hardware - stick as close to resonant antenna frequencies as possible
1. Collect noise floor readings from various points in town using SDR for the candidate frequency slots
    - Ensure that we collect measurements at the same locations as our key nodes identified above
1. Based on [noise floor measurements](noise-floor-measurements/README.md) collected from strategic locations, choose the frequency slot for the test
1. Agree upon a consistent firmware version that will be used for the duration of the test to minimize variables
    - In the real world, nodes will be on a variety of firmware versions, and we cannot reasonably control this variable.
1. Set up ***new*** nodes on the new frequency slot, ***still using LongFast***.  
    - Data should be reported to Bridger.
    - Discuss with Andy if we can report data to a segregated MQTT topic path for independent visualization of the data for this test.
        - For preset changes both the ServiceEnvelope `channel_id` and MQTT topic name change. This would allow us to filter metrics on `channel_id`. But it requires separate MQTT logins since those are tied to a specific topic per radio which has `LongFast` in the tpic name.
        - For a frequency slot change we wouldn't have any way to distinguish those packets over MQTT as they don't appear to be sent as any parameter.
    - Make a point to utilize this parallel mesh as much as possible to properly gauge its health.
    - Run this parallel mesh with LongFast for at least a week.
1. Switch the new nodes to MediumFast and let it run for at least a week.
1. Document observations with real world usage examples and recorded data from Bridger.
    - Hopefully arrive at some lessons learned that can be applied to improving our network, regardless of whether that results in changing frequencies or modem presets in the short/long term.

## Key Nodes

TBD (contributions welcome)

## Metrics to Evaluate

TBD (contributions welcome)

## References

1. [Modem Presets](https://meshtastic.org/docs/overview/radio-settings/#presets)
1. [Frequency Slots](https://meshtastic.org/docs/overview/radio-settings/#frequency-slot-calculator)
1. [Bridger Graphs](https://graphs.austinmesh.org/) and [source](https://github.com/austinmesh/bridger)
