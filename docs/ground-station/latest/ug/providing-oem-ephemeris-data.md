# Provide OEM ephemeris data

###### Important

The ephemeris API is currently in a Preview state

Access to the Ephemeris API is provided only on an as-needed basis. If you require the ability
to upload custom ephemeris data, you should contact `<aws-groundstation@amazon.com>`.

## Overview

Orbit Ephemeris Message (OEM) is a standardized format for representing spacecraft trajectory data. The Ephemeris
API allows OEM ephemerides to be uploaded to AWS Ground Station for use with a satellite. These ephemerides override the
default ephemerides from [Space-Track](https://www.space-track.org/ "https://www.space-track.org/") (see:
[Default ephemeris data](default-ephemeris-data.md "default-ephemeris-data.md")).

AWS Ground Station treats ephemerides as [Individualized
Usage Data](https://aws.amazon.com/service-terms "https://aws.amazon.com/service-terms"). If you use this optional feature, AWS will use your ephemeris data to provide
troubleshooting support.

Uploading custom OEM ephemerides can improve the quality of tracking, handle early operations where no
[Space-Track](https://www.space-track.org/ "https://www.space-track.org/") ephemerides are available to AWS Ground Station,
and account for maneuvers.

###### Note

When providing custom ephemeris before a satellite catalog number is assigned for your
satellite, you can use `satelliteId` for the `OBJECT_ID` portion of the OEM.

For more information about the format of OEMs, see [OEM ephemeris format](#oem-ephemeris-format "#oem-ephemeris-format").

## OEM ephemeris format

AWS Ground Station processes OEM Customer Provided Ephemerides according to the
[CCSDS standard](https://ccsds.org/wp-content/uploads/gravity_forms/5-448e85c647331d9cbaf66c096458bdd5/2025/01//502x0b3e1.pdf "https://ccsds.org/wp-content/uploads/gravity_forms/5-448e85c647331d9cbaf66c096458bdd5/2025/01//502x0b3e1.pdf")
with some extra restrictions. OEM files should be in KVN format. The following table outlines the different fields
in an OEM and how AWS Ground Station differs from the CCSDS standard.

| Section              | Field            | CCSDS required  | AWS Ground Station required                                                        | Notes               |
| -------------------- | ---------------- | --------------- | ---------------------------------------------------------------------------------- | ------------------- |
| Header               | CCSDS_OEM_VERS   | Yes             | Yes                                                                                | Required value: 2.0 |
| COMMENT              | No               | No              |                                                                                    |
| CLASSIFICATION       | No               | No              |                                                                                    |
| CREATION_DATE        | Yes              | Yes             |                                                                                    |
| ORIGINATOR           | Yes              | Yes             |                                                                                    |
| MESSAGE_ID           | No               | No              |                                                                                    |
| Metadata             | META_START       | Yes             | Yes                                                                                |                     |
| COMMENT              | No               | No              |                                                                                    |
| OBJECT_NAME          | Yes              | Yes             |                                                                                    |
| OBJECT_ID            | Yes              | Yes             |                                                                                    |
| CENTER_NAME          | Yes              | Yes             | Required value: Earth                                                              |
| REF_FRAME            | Yes              | Yes             | Accepted values: EME2000, ITRF2000                                                 |
| REF_FRAME_EPOCH      | No               | Not supported\* | Not needed because the accepted REF_FRAMEs have an implicit epoch                  |
| TIME_SYSTEM          | Yes              | Yes             | Required value: UTC                                                                |
| START_TIME           | Yes              | Yes             |                                                                                    |
| USEABLE_START_TIME   | No               | No              |                                                                                    |
| USEABLE_STOP_TIME    | No               | No              |                                                                                    |
| STOP_TIME            | Yes              | Yes             |                                                                                    |
| INTERPOLATION        | No               | Yes             | Required so AWS Ground Station can generate accurate pointing angles for contacts. |
| INTERPOLATION_DEGREE | No               | Yes             | Required so AWS Ground Station can generate accurate pointing angles for contacts. |
| META_STOP            | Yes              | Yes             |                                                                                    |
| Data                 | X                | Yes             | Yes                                                                                | Represented in `km` |
| Y                    | Yes              | Yes             | Represented in `km`                                                                |
| Z                    | Yes              | Yes             | Represented in `km`                                                                |
| X_DOT                | Yes              | Yes             | Represented in `km/s`                                                              |
| Y_DOT                | Yes              | Yes             | Represented in `km/s`                                                              |
| Z_DOT                | Yes              | Yes             | Represented in `km/s`                                                              |
| X_DDOT               | No               | No              | Represented in `km/s^2`                                                            |
| Y_DDOT               | No               | No              | Represented in `km/s^2`                                                            |
| Z_DDOT               | No               | No              | Represented in `km/s^2`                                                            |
| Covariance matrix    | COVARIANCE_START | No              | No                                                                                 |                     |
| EPOCH                | No               | No              |                                                                                    |
| COV_REF_FRAME        | No               | No              |                                                                                    |
| COVARIANCE_STOP      | No               | No              |                                                                                    |

\* If any rows that aren't supported by AWS Ground Station are included in the provided OEM, the OEM will fail validation.

The important deviations from the CCSDS standard for AWS Ground Station are:

- `CCSDS_OEM_VERS` is required to be `2.0`.
- `REF_FRAME` is required to be either `EME2000` or `ITRF2000`.
- `REF_FRAME_EPOCH` is not supported by AWS Ground Station.
- `CENTER_NAME` is required to be `Earth`.
- `TIME_SYSTEM` is required to be `UTC`.
- `INTERPOLATION` and `INTERPOLATION_DEGREE` are both required for AWS Ground Station customer provided ephemeris.

## Example OEM ephemeris in KVN format

Following is a truncated example of an OEM ephemeris in KVN format for the JPSS-1 public broadcaster satellite.

```
CCSDS_OEM_VERS = 2.0

COMMENT Orbit data are consistent with planetary ephemeris DE-430

CREATION_DATE  = 2024-07-22T05:20:59
ORIGINATOR     = Raytheon-JPSS/CGS

META_START
OBJECT_NAME          = J1
OBJECT_ID            = 2017-073A
CENTER_NAME          = Earth
REF_FRAME            = EME2000
TIME_SYSTEM          = UTC
START_TIME           = 2024-07-22T00:00:00.000000
STOP_TIME            = 2024-07-22T00:06:00.000000
INTERPOLATION        = Lagrange
INTERPOLATION_DEGREE = 5
META_STOP

2024-07-22T00:00:00.000000   5.905147360000000e+02  -1.860082793999999e+03  -6.944807075000000e+03  -5.784245796000000e+00   4.347501391999999e+00  -1.657256863000000e+00
2024-07-22T00:01:00.000000   2.425572045154201e+02  -1.595860765983339e+03  -7.030938457373539e+03  -5.810660250794190e+00   4.457103652219009e+00  -1.212889340333023e+00
2024-07-22T00:02:00.000000  -1.063224256538050e+02  -1.325569732497146e+03  -7.090262617183503e+03  -5.814973972202444e+00   4.549739160042560e+00  -7.639633689161465e-01
2024-07-22T00:03:00.000000  -4.547973959231161e+02  -1.050238305712201e+03  -7.122556683227951e+03  -5.797176562437553e+00   4.625064829516728e+00  -3.121687831090774e-01
2024-07-22T00:04:00.000000  -8.015427368657785e+02  -7.709137891269565e+02  -7.127699477194810e+03  -5.757338007808417e+00   4.682800822515077e+00   1.407953645161997e-01
2024-07-22T00:05:00.000000  -1.145240083085062e+03  -4.886583601179489e+02  -7.105671911254255e+03  -5.695608435738609e+00   4.722731329786999e+00   5.932259682105052e-01
2024-07-22T00:06:00.000000  -1.484582479061495e+03  -2.045451985605701e+02  -7.056557069672793e+03  -5.612218005854990e+00   4.744705579872771e+00   1.043421397392599e+00
```

## Creating an OEM ephemeris

An OEM ephemeris can be created using the
[CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md") action in the AWS Ground Station API.
This action will upload an ephemeris using data either in the request body or from a specified S3 bucket.

It is important to note that uploading an ephemeris sets the ephemeris to `VALIDATING` and starts an asynchronous
workflow that will validate and generate potential contacts from your ephemeris. Only once an ephemeris has passed
this workflow and become `ENABLED` will it be used for contacts.
You should poll [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md")
for the ephemeris status or use CloudWatch events to track the ephemeris' status changes.

To troubleshoot an invalid ephemeris see:
[Troubleshoot invalid ephemerides](troubleshooting-invalid-ephemerides.md "troubleshooting-invalid-ephemerides.md")

## Example: Uploading OEM ephemeris data from an S3 bucket

It is also possible to upload an OEM ephemeris file directly from an S3 bucket by pointing to the bucket and object
key. AWS Ground Station will retrieve the object on your behalf. Information about the encryption of data at rest
in AWS Ground Station is detailed in: [Data encryption at rest for AWS Ground Station](security.md "security.md").

Below is an example of uploading an OEM ephemeris file from an S3 bucket

```
import boto3
from datetime import datetime, timedelta, timezone

# Create AWS clients
s3_client = boto3.client("s3")
ground_station_client = boto3.client("groundstation")

# Define S3 bucket and key
bucket_name = "ephemeris-bucket"
object_key = "test_data.oem"

# Create sample OEM data in KVN format
oem_data = """CCSDS_OEM_VERS = 2.0

COMMENT Orbit data are consistent with planetary ephemeris DE-430

CREATION_DATE  = 2024-07-22T05:20:59
ORIGINATOR     = Raytheon-JPSS/CGS

META_START
OBJECT_NAME          = J1
OBJECT_ID            = 2017-073A
CENTER_NAME          = Earth
REF_FRAME            = EME2000
TIME_SYSTEM          = UTC
START_TIME           = 2024-07-22T00:00:00.000000
STOP_TIME            = 2024-07-22T00:06:00.000000
INTERPOLATION        = Lagrange
INTERPOLATION_DEGREE = 5
META_STOP

2024-07-22T00:00:00.000000   5.905147360000000e+02  -1.860082793999999e+03  -6.944807075000000e+03  -5.784245796000000e+00   4.347501391999999e+00  -1.657256863000000e+00
2024-07-22T00:01:00.000000   2.425572045154201e+02  -1.595860765983339e+03  -7.030938457373539e+03  -5.810660250794190e+00   4.457103652219009e+00  -1.212889340333023e+00
2024-07-22T00:02:00.000000  -1.063224256538050e+02  -1.325569732497146e+03  -7.090262617183503e+03  -5.814973972202444e+00   4.549739160042560e+00  -7.639633689161465e-01
2024-07-22T00:03:00.000000  -4.547973959231161e+02  -1.050238305712201e+03  -7.122556683227951e+03  -5.797176562437553e+00   4.625064829516728e+00  -3.121687831090774e-01
2024-07-22T00:04:00.000000  -8.015427368657785e+02  -7.709137891269565e+02  -7.127699477194810e+03  -5.757338007808417e+00   4.682800822515077e+00   1.407953645161997e-01
2024-07-22T00:05:00.000000  -1.145240083085062e+03  -4.886583601179489e+02  -7.105671911254255e+03  -5.695608435738609e+00   4.722731329786999e+00   5.932259682105052e-01
2024-07-22T00:06:00.000000  -1.484582479061495e+03  -2.045451985605701e+02  -7.056557069672793e+03  -5.612218005854990e+00   4.744705579872771e+00   1.043421397392599e+00
"""

# Upload sample OEM data to S3
print(f"Uploading OEM data to s3://{bucket_name}/{object_key}")

s3_client.put_object(
    Bucket=bucket_name, Key=object_key, Body=oem_data, ContentType="text/plain"
)

print("OEM data uploaded successfully to S3")

# Create OEM ephemeris from S3
print("Creating OEM ephemeris from S3...")

s3_oem_ephemeris = ground_station_client.create_ephemeris(
    name="2024-07-22 S3 OEM Upload",
    satelliteId="fde41049-14f7-413e-bd7b-EXAMPLE01",
    enabled=True,
    expirationTime=datetime.now(timezone.utc) + timedelta(days=5),
    priority=2,
    ephemeris={"oem": {"s3Object": {"bucket": bucket_name, "key": object_key}}},
)

print(f"Created OEM ephemeris with ID: {s3_oem_ephemeris['ephemerisId']}")

```

Below is an example returned data from the
[DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") action being called for the OEM
ephemeris uploaded in the previous block of example code.

```
{
  "creationTime": 1620254718.765,
  "enabled": true,
  "name": "Example Ephemeris",
  "ephemerisId": "fde41049-14f7-413e-bd7b-EXAMPLE02",
  "priority": 2,
  "status": "VALIDATING",
  "suppliedData": {
    "oem": {
      "sourceS3Object": {
          "bucket": "ephemeris-bucket-for-testing",
          "key": "test_data.oem"
      }
    }
  }
}
```
