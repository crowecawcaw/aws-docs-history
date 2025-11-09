# Provide custom ephemeris data

###### Important

The ephemeris API is currently in a Preview state

Access to the Ephemeris API is provided only on an as-needed basis. If you require the ability
to upload custom ephemeris data, you should contact `<aws-groundstation@amazon.com>`.

## Overview

The Ephemeris API allows custom ephemerides to be uploaded to AWS Ground Station for use with a
satellite. These ephemerides override the default ephemerides from
[Space-Track](https://www.space-track.org/ "https://www.space-track.org/") (see:
[Default ephemeris data](default-ephemeris-data.md "default-ephemeris-data.md")).
We support receiving ephemeris data in Orbit Ephemeris Message (OEM), two-line element
(TLE), and azimuth elevation formats.

AWS Ground Station treats ephemerides as [Individualized
Usage Data](https://aws.amazon.com/service-terms "https://aws.amazon.com/service-terms"). If you use this optional feature, AWS will use your ephemeris data to provide
troubleshooting support.

Uploading custom ephemerides can improve the quality of tracking, handle operations where no [Space-Track](https://www.space-track.org/ "https://www.space-track.org/")
ephemerides are available to AWS Ground Station, and account for maneuvers.

To troubleshoot an invalid ephemeris see:
[Troubleshoot invalid ephemerides](troubleshooting-invalid-ephemerides.md "troubleshooting-invalid-ephemerides.md")

## Example: Using customer-provided ephemerides with AWS Ground Station

For more detailed instructions for using customer-provided ephemerides with AWS Ground Station, see
[Using customer-provided ephemerides with
AWS Ground Station](https://aws.amazon.com/blogs/publicsector/using-customer-provided-ephemerides-with-aws-ground-station/ "https://aws.amazon.com/blogs/publicsector/using-customer-provided-ephemerides-with-aws-ground-station/") and it's associated GitHub repository [aws-samples/aws-groundstation-cpe](https://github.com/aws-samples/aws-groundstation-cpe "https://github.com/aws-samples/aws-groundstation-cpe").
