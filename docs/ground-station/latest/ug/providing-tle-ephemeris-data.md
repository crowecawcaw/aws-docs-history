# Provide TLE ephemeris data

###### Important

The ephemeris API is currently in a Preview state

Access to the Ephemeris API is provided only on an as-needed basis. If you require the ability
to upload custom ephemeris data, you should contact `<aws-groundstation@amazon.com>`.

## Overview

Two-line element (TLE) sets are a standardized format for describing satellite orbits. The Ephemeris API allows
TLE ephemerides to be uploaded to AWS Ground Station for use with a satellite. These ephemerides override the default
ephemerides from [Space-Track](https://www.space-track.org/ "https://www.space-track.org/") (see:
[Default ephemeris data](default-ephemeris-data.md "default-ephemeris-data.md")).

AWS Ground Station treats ephemerides as [Individualized
Usage Data](https://aws.amazon.com/service-terms "https://aws.amazon.com/service-terms"). If you use this optional feature, AWS will use your ephemeris data to provide
troubleshooting support.

Uploading custom TLE ephemerides can improve the quality of tracking, handle early operations where no
[Space-Track](https://www.space-track.org/ "https://www.space-track.org/") ephemerides are available to AWS Ground Station,
and account for maneuvers.

###### Note

When providing custom ephemeris before a satellite catalog number is assigned for your
satellite, you can use `00000` for the satellite catalog number field of the TLE, and `000` for
the launch number portion of the international designator field of the TLE (e.g. `24000A` for a vehicle
launched in 2024).

For more information about the format of TLEs, see
[Two-line element set](https://en.wikipedia.org/wiki/Two-line_element_set "https://en.wikipedia.org/wiki/Two-line_element_set").

## Creating a TLE ephemeris

A TLE ephemeris can be created using the [CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md") action in the AWS Ground Station
API. This action will upload an ephemeris using data either in the request body or from a specified S3 bucket.

It is important to note that uploading an ephemeris sets the ephemeris to `VALIDATING` and starts an asynchronous
workflow that will validate and generate potential contacts from your ephemeris. Only once an ephemeris has passed
this workflow and become `ENABLED` will it be used for contacts. You should poll [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md")
for the ephemeris status or use CloudWatch events to track the ephemeris' status changes.

To troubleshoot an invalid ephemeris see:
[Troubleshoot invalid ephemerides](troubleshooting-invalid-ephemerides.md "troubleshooting-invalid-ephemerides.md")

## Example: Create a two-line element (TLE) set ephemeris via API

The AWS SDKs, and CLI can be used to upload a two line element (TLE) set ephemeris to AWS Ground Station via
the [CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md") call.
This ephemeris will be used in place of the default ephemeris data
for a satellite (see [Default ephemeris data](default-ephemeris-data.md "default-ephemeris-data.md")). This example
shows how to do this using the [AWS SDK for Python (Boto3)](../../../pythonsdk.md "../../../pythonsdk.md").

A TLE set is a JSON formatted object that strings one or more TLEs together to construct a continuous trajectory.
The TLEs in the TLE set must form a continuous set that we can use to construct a trajectory (i.e. no gaps in time
between TLEs in a TLE set). An example TLE set is shown below:

```
[
    {
        "tleLine1": "1 25994U 99068A   20318.54719794  .00000075  00000-0  26688-4 0  9997",
        "tleLine2": "2 25994  98.2007  30.6589 0001234  89.2782  18.9934 14.57114995111906",
        "validTimeRange": {
            "startTime": 12345,
            "endTime": 12346
        }
    },
    {
        "tleLine1": "1 25994U 99068A   20318.54719794  .00000075  00000-0  26688-4 0  9997",
        "tleLine2": "2 25994  98.2007  30.6589 0001234  89.2782  18.9934 14.57114995111906",
        "validTimeRange": {
            "startTime": 12346,
            "endTime": 12347
        }
    }
]
```

###### Note

The time ranges of the TLEs in a TLE set must match up exactly to be a valid, continuous trajectory.

A TLE set can be uploaded via the AWS Ground Station boto3 client as follows:

```
import boto3
from datetime import datetime, timedelta, timezone

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# Create TLE ephemeris
tle_ephemeris = ground_station_client.create_ephemeris(
    name="Example Ephemeris",
    satelliteId="2e925701-9485-4644-b031-EXAMPLE01",
    enabled=True,
    expirationTime=datetime.now(timezone.utc) + timedelta(days=3),
    priority=2,
    ephemeris={
        "tle": {
            "tleData": [
                {
                    "tleLine1": "1 25994U 99068A   20318.54719794  .00000075  00000-0  26688-4 0  9997",
                    "tleLine2": "2 25994  98.2007  30.6589 0001234  89.2782  18.9934 14.57114995111906",
                    "validTimeRange": {
                        "startTime": datetime.now(timezone.utc),
                        "endTime": datetime.now(timezone.utc) + timedelta(days=7),
                    },
                }
            ]
        }
    },
)

print(f"Created TLE ephemeris with ID: {tle_ephemeris['ephemerisId']}")

```

This call will return an ephemerisId that can be used to reference the ephemeris in the future. For example, we can
use the provided ephemerisId from the call above to poll for the status of the ephemeris:

```
import boto3
from datetime import datetime, timedelta, timezone
import time

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# First, create a TLE ephemeris
print("Creating TLE ephemeris...")

tle_ephemeris = ground_station_client.create_ephemeris(
    name="Example TLE Ephemeris for Description",
    satelliteId="2e925701-9485-4644-b031-EXAMPLE01",
    enabled=True,
    expirationTime=datetime.now(timezone.utc) + timedelta(days=3),
    priority=2,
    ephemeris={
        "tle": {
            "tleData": [
                {
                    "tleLine1": "1 25994U 99068A   20318.54719794  .00000075  00000-0  26688-4 0  9997",
                    "tleLine2": "2 25994  98.2007  30.6589 0001234  89.2782  18.9934 14.57114995111906",
                    "validTimeRange": {
                        "startTime": datetime.now(timezone.utc),
                        "endTime": datetime.now(timezone.utc) + timedelta(days=7),
                    },
                }
            ]
        }
    },
)

ephemeris_id = tle_ephemeris["ephemerisId"]
print(f"Created TLE ephemeris with ID: {ephemeris_id}")

# Describe the ephemeris immediately to check initial status
print("Describing ephemeris...")

response = ground_station_client.describe_ephemeris(ephemerisId=ephemeris_id)

print(f"Ephemeris ID: {response['ephemerisId']}")
print(f"Name: {response['name']}")
print(f"Status: {response['status']}")

```

An example response from the [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") action is provided below

```
{
  "creationTime": 1620254718.765,
  "enabled": true,
  "name": "Example Ephemeris",
  "ephemerisId": "fde41049-14f7-413e-bd7b-EXAMPLE01",
  "priority": 2,
  "status": "VALIDATING",
  "suppliedData": {
    "tle": {
      "ephemerisData": "[{\"tleLine1\": \"1 25994U 99068A   20318.54719794  .00000075  00000-0  26688-4 0  9997\",\"tleLine2\": \"2 25994  98.2007  30.6589 0001234  89.2782  18.9934 14.57114995111906\",\"validTimeRange\": {\"startTime\": 1620254712000,\"endTime\": 1620859512000}}]"
    }
  }
}
```

It is recommended to poll the [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") route or use CloudWatch events to track the
status of the uploaded ephemeris as it must go through an asynchronous validation workflow before it is set to
`ENABLED` and becomes usable for scheduling and executing contacts.

Note that the NORAD ID in all TLEs in the TLE set, `25994` in the examples above, must match the NORAD ID your
satellite has been assigned in the [Space-Track](https://www.space-track.org/ "https://www.space-track.org/") database.

## Example: Uploading TLE ephemeris data from an S3 bucket

It is also possible to upload a TLE ephemeris file directly from an S3 bucket by pointing to the bucket and object
key. AWS Ground Station will retrieve the object on your behalf. Information about the encryption of data at rest
in AWS Ground Station is detailed in: [Data encryption at rest for AWS Ground Station](security.md "security.md").

Below is an example of uploading a TLE ephemeris file from an S3 bucket

```
import boto3
from datetime import datetime, timedelta, timezone
import json

# Create AWS clients
s3_client = boto3.client("s3")
ground_station_client = boto3.client("groundstation")

# Define S3 bucket and key
bucket_name = "ephemeris-bucket"
object_key = "test_data.tle"

# Create sample TLE set data
# Note: For actual satellites, use real TLE data from sources like Space-Track
tle_set_data = [
    {
        "tleLine1": "1 25994U 99068A   20318.54719794  .00000075  00000-0  26688-4 0  9997",
        "tleLine2": "2 25994  98.2007  30.6589 0001234  89.2782  18.9934 14.57114995111906",
        "validTimeRange": {
            "startTime": datetime.now(timezone.utc),
            "endTime": datetime.now(timezone.utc) + timedelta(days=3),
        },
    },
    {
        "tleLine1": "1 25994U 99068A   20321.54719794  .00000075  00000-0  26688-4 0  9998",
        "tleLine2": "2 25994  98.2007  33.6589 0001234  89.2782  18.9934 14.57114995112342",
        "validTimeRange": {
            "startTime": datetime.now(timezone.utc) + timedelta(days=3),
            "endTime": datetime.now(timezone.utc) + timedelta(days=7),
        },
    },
]

# Convert to JSON string for upload
tle_json = json.dumps(tle_set_data, indent=2)

# Upload sample TLE data to S3
print(f"Uploading TLE set data to s3://{bucket_name}/{object_key}")

s3_client.put_object(
    Bucket=bucket_name, Key=object_key, Body=tle_json, ContentType="application/json"
)
print("TLE set data uploaded successfully to S3")
print(f"Uploaded {len(tle_set_data)} TLE entries covering 7 days")

# Create TLE ephemeris from S3
print("Creating TLE ephemeris from S3...")

s3_tle_ephemeris = ground_station_client.create_ephemeris(
    name="2022-11-05 S3 TLE Upload",
    satelliteId="fde41049-14f7-413e-bd7b-EXAMPLE01",
    enabled=True,
    expirationTime=datetime.now(timezone.utc) + timedelta(days=5),
    priority=2,
    ephemeris={"tle": {"s3Object": {"bucket": bucket_name, "key": object_key}}},
)

print(f"Created TLE ephemeris with ID: {s3_tle_ephemeris['ephemerisId']}")

```
