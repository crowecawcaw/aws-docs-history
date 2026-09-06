

# Provide TLE ephemeris data
<a name="providing-tle-ephemeris-data"></a>

**Important**  
 The ephemeris API is currently in a Preview state 

 Access to the Ephemeris API is provided only on an as-needed basis. If you require the ability to upload custom ephemeris data, please open an AWS Support ticket through the [AWS Support Center Console](https://console.aws.amazon.com/support). Our team will work with you to enable this capability for your specific requirements. 

## Overview
<a name="w2aac28c17c11b7"></a>

 Two-line element (TLE) sets are a standardized format for describing satellite orbits. The Ephemeris API allows TLE ephemerides to be uploaded to AWS Ground Station for use with a satellite. These ephemerides override the default ephemerides from [Space-Track](https://www.space-track.org/) (see: [Default ephemeris data](default-ephemeris-data.md)). 

 AWS Ground Station treats ephemerides as [Individualized Usage Data](https://aws.amazon.com/service-terms). If you use this optional feature, AWS will use your ephemeris data to provide troubleshooting support. 

 Uploading custom TLE ephemerides can improve the quality of tracking, handle early operations where no [Space-Track](https://www.space-track.org/) ephemerides are available to AWS Ground Station, and account for maneuvers. However, TLE accuracy is limited by the propagation model and degrades over time away from epoch. For higher-fidelity ephemeris data over longer time spans, consider using OEM format (see [Provide OEM ephemeris data](providing-oem-ephemeris-data.md)). 

**Note**  
 When providing custom ephemeris before a satellite catalog number is assigned for your satellite, you can use `00000` for the satellite catalog number field of the TLE, and `000` for the launch number portion of the international designator field of the TLE (e.g. `24000A` for a vehicle launched in 2024).   
 For more information about the format of TLEs, see [Two-line element set](https://en.wikipedia.org/wiki/Two-line_element_set). 

## Alpha-5 satellite catalog numbers in TLEs
<a name="w2aac28c17c11b9"></a>

 Two-Line Element sets (TLEs) use a fixed-width format in which the satellite catalog number field (columns 3–7 of lines 1 and 2) is limited to 5 digits, supporting a maximum value of 99,999. To represent satellite catalog numbers beyond this limit, the United States Space Force developed the [Alpha-5](https://www.space-track.org/documentation#tle-alpha5) encoding scheme. Alpha-5 replaces the first digit of the satellite catalog number field with an alphabetic character (A–Z, excluding I and O to avoid confusion with digits 1 and 0). This extends the range of representable satellite catalog numbers from 100,000 to 339,999 within the existing fixed-width TLE format. 

 Alpha-5 is purely a display encoding for the TLE text format. The underlying numeric satellite catalog number does not change. The `noradSatelliteID` field in the AWS Ground Station API remains an integer — API responses such as `ListSatellites` and `GetSatellite` continue to return the numeric satellite catalog number, not the Alpha-5 encoded form. Alpha-5 encoding is only relevant within the TLE text lines themselves. 

 AWS Ground Station supports TLE ephemerides that contain Alpha-5 encoded satellite numbers. When you upload a TLE through the [CreateEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEphemeris.html) action, AWS Ground Station correctly parses Alpha-5 encoded satellite numbers and resolves them to the corresponding integer satellite catalog numbers internally. Satellites with satellite catalog numbers in the Alpha-5 range (100,000–339,999) are fully supported. 

 The following is an example TLE set for a satellite with satellite catalog number 100,000. The Alpha-5 encoding represents this as `A0000` in columns 3–7 of each TLE line: 

```
[
    {
        "tleLine1": "1 A0000U 26001A   26120.50000000  .00000072  00000-0  24500-4 0  9991",
        "tleLine2": "2 A0000  97.4500  85.2300 0012345  45.6789 314.5678 15.20000000 10013",
        "validTimeRange": {
            "startTime": 1777680000,
            "endTime": 1778284800
        }
    }
]
```

 For more information about the Alpha-5 encoding scheme, see the [Space-Track Alpha-5 documentation](https://www.space-track.org/documentation#tle-alpha5). 

## Creating a TLE ephemeris
<a name="w2aac28c17c11c11"></a>

 A TLE ephemeris can be created using the [CreateEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEphemeris.html) action in the AWS Ground Station API. This action will upload an ephemeris using data either in the request body or from a specified S3 bucket. 

 It is important to note that uploading an ephemeris sets the ephemeris to `VALIDATING` and starts an asynchronous workflow that will validate and generate potential contacts from your ephemeris. Only once an ephemeris has passed this workflow and become `ENABLED` will it be used for contacts. You should poll [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) for the ephemeris status or use CloudWatch events to track the ephemeris' status changes. 

 To troubleshoot an invalid ephemeris see: [Troubleshoot invalid ephemerides](troubleshooting-invalid-ephemerides.md) 

## Example: Create a two-line element (TLE) set ephemeris via API
<a name="w2aac28c17c11c13"></a>

 The AWS SDKs, and CLI can be used to upload a two line element (TLE) set ephemeris to AWS Ground Station via the [CreateEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEphemeris.html) call. This ephemeris will be used in place of the default ephemeris data for a satellite (see [Default ephemeris data](default-ephemeris-data.md)). This example shows how to do this using the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/pythonsdk). 

 A TLE set is a JSON formatted object that strings one or more TLEs together to construct a continuous trajectory. The TLEs in the TLE set must form a continuous set that we can use to construct a trajectory (i.e. no gaps in time between TLEs in a TLE set). An example TLE set is shown below: 

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

**Note**  
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

 This call will return an ephemerisId that can be used to reference the ephemeris in the future. For example, we can use the provided ephemerisId from the call above to poll for the status of the ephemeris: 

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

 An example response from the [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) action is provided below 

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

 It is recommended to poll the [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) route or use CloudWatch events to track the status of the uploaded ephemeris as it must go through an asynchronous validation workflow before it is set to `ENABLED` and becomes usable for scheduling and executing contacts. 

 Note that the NORAD ID in all TLEs in the TLE set, `25994` in the examples above, must match the NORAD ID your satellite has been assigned in the [Space-Track](https://www.space-track.org/) database. 

## Example: Uploading TLE ephemeris data from an S3 bucket
<a name="w2aac28c17c11c15"></a>

 It is also possible to upload a TLE ephemeris file directly from an S3 bucket by pointing to the bucket and object key. AWS Ground Station will retrieve the object on your behalf. Information about the encryption of data at rest in AWS Ground Station is detailed in: [Data encryption at rest for AWS Ground Station](security.encryption-at-rest.md). 

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