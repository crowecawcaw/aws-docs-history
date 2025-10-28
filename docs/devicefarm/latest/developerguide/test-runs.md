# Runs in AWS Device Farm

The following sections contain information about runs in Device Farm.

A run in Device Farm represents a specific build of your app, with a specific set of tests, to be run on a specific set of devices.
A run produces a report that contains information about the results of the run. A run contains one or more jobs.

###### Topics

- [Run configuration](#test-runs-configuration "#test-runs-configuration")
- [Run files retention](#test-runs-retention "#test-runs-retention")
- [Run device state](#test-runs-device-state "#test-runs-device-state")
- [Parallel runs](#test-runs-parallel "#test-runs-parallel")
- [Setting the execution timeout](#test-runs-default-timeout "#test-runs-default-timeout")
- [Ads in runs](#test-runs-ads "#test-runs-ads")
- [Media in runs](#test-runs-media "#test-runs-media")
- [Common tasks for runs](#test-runs-tasks "#test-runs-tasks")

## Run configuration

As part of a run, you can supply settings Device Farm can use to override current device
settings. These include latitude and longitude coordinates, locale, radio states (such
as Bluetooth, GPS, NFC, and Wi-Fi), extra data (contained in a .zip file), and auxiliary
apps (apps that should be installed before the app to be tested).

## Run files retention

Device Farm stores your apps and files for 30 days and then deletes them from its system.
You can delete your files at any time, however.

Device Farm stores your run results, logs, and screenshots for 400 days and then deletes
them from its system.

## Run device state

Device Farm always reboots a device before making it available for the next job.

## Parallel runs

Device Farm runs tests in parallel as devices become available.

## Setting the execution timeout

You can set a value for how long a test run should execute before you stop each device
from running a test. For example, if your tests take 20 minutes per device to complete, you
should choose a timeout of 30 minutes per device.

For more information, see [Setting the execution timeout for test runs in
AWS Device Farm](how-to-set-default-timeout-for-test-runs.md "how-to-set-default-timeout-for-test-runs.md").

## Ads in runs

We recommend that you remove ads from your apps before you upload them to Device Farm. We
cannot guarantee that ads are displayed during runs.

## Media in runs

You can provide media or other data to accompany your app. Additional data must be
provided in a .zip file no more than 4 GB in size.

## Common tasks for runs

For more information, see [Creating a test run in Device Farm](how-to-create-test-run.md "how-to-create-test-run.md") and [Test runs in AWS Device Farm](runs.md "runs.md").
