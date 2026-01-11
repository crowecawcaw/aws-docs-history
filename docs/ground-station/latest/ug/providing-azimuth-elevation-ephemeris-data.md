# Provide azimuth elevation ephemeris data

###### Important

The azimuth elevation ephemeris feature is currently in a Preview state and requires explicit onboarding.

Azimuth elevation ephemeris functionality is under strict access control for a
limited number of pre-determined, specialized use cases. Access is
significantly more restrictive than for standard customer-provided
ephemeris capabilities. For more information about approved use cases and
the access request process, please open an AWS Support ticket through the
[AWS Support Center Console](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").
Our team will guide you through the approval process for specialized use cases.

## Overview

Azimuth elevation ephemeris provides a way to directly specify antenna pointing directions without providing satellite
orbital information. Instead of uploading ephemeris data that describes a satellite's orbit, you provide
time-tagged azimuth and elevation angles that tell the antenna exactly where to point throughout
a contact.

AWS Ground Station treats ephemerides as [Individualized
Usage Data](https://aws.amazon.com/service-terms "https://aws.amazon.com/service-terms"). If you use this optional feature, AWS will use your ephemeris data to provide
troubleshooting support.

This approach is particularly useful for the following scenarios:

- _Early operations support:_ During Launch and Early Orbit Phase (LEOP) when
  precise orbital data is unavailable, or orbital parameters are rapidly changing.
- _Custom pointing patterns:_ Implementing specific pointing sequences for
  antenna testing or non-standard operations.

###### Note

When using azimuth elevation ephemeris, the satellite ARN may be omitted from the contact reservation request.
If the satellite ARN is not omitted, it will still be included as part of the contact data, but the azimuth
elevation ephemeris will be used for antenna pointing rather than performing ephemeris priority resolution.
The azimuth elevation ephemeris is associated with a specific ground station and defines the antenna pointing
directions for that location.

## Azimuth elevation ephemeris data format

Azimuth elevation ephemeris data consists of time-tagged azimuth and elevation values organized into segments.
Each segment contains a series of azimuth and elevation angles that cover a specific time range.

The key components of azimuth elevation ephemeris data are:

- _Ground Station:_ The specific ground station where this azimuth elevation ephemeris
  will be used.
- _Angle Unit:_ The unit of measurement for angles (`DEGREE_ANGLE` or `RADIAN`).
- _Segments:_ One or more time-bounded collections of azimuth and elevation angles.
- _Time-tagged angles:_ Individual azimuth and elevation values with associated timestamps.

Each segment requires:

- A reference epoch (the base time for the segment)
- A valid time range (start and end times for the segment)
- At least 5 time-tagged azimuth/elevation pairs

Azimuth elevation constraints:

- Azimuth in degrees: -180° to 360°
- Azimuth in radians: -π to 2π
- Elevation in degrees: -90° to 90°
- Elevation in radians: -π/2 to π/2
- Time values must be in ascending order within each segment
- Segments must not overlap in time

For more information, see the [CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md")
API documentation and the [TimeAzEl](../APIReference/API_TimeAzEl.md "../APIReference/API_TimeAzEl.md") data type.

## Creating azimuth elevation ephemeris

Azimuth elevation ephemeris is created using the same [CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md") API action,
but with the `azEl` ephemeris type. The key differences from TLE and OEM ephemeris are:

- You must specify a `groundStation` parameter
- The `satelliteId` parameter must be omitted from the request
- Priority settings do not apply (each azimuth elevation ephemeris is specific to a ground station)
- Each segment must contain at least 5 azimuth/elevation points to support 4th order Lagrange interpolation
- Additional limits and requirements are detailed in the [CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md") API documentation

It is important to note that uploading an ephemeris sets the ephemeris to `VALIDATING` and starts an asynchronous
workflow that will validate and generate potential contacts from your ephemeris.
An ephemeris will only be used for contacts after it has passed this workflow and its status becomes `ENABLED`.
You should poll [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md")
for the ephemeris status or use CloudWatch events to track the ephemeris' status changes.

To troubleshoot an invalid ephemeris see:
[Troubleshoot invalid ephemerides](troubleshooting-invalid-ephemerides.md "troubleshooting-invalid-ephemerides.md")

## Example: Create azimuth elevation ephemeris via API

The following example shows how to create an azimuth elevation ephemeris using the AWS SDK for Python (Boto3):

```
import boto3

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# Create azimuth elevation ephemeris
azimuth_elevation_ephemeris = ground_station_client.create_ephemeris(
    name="Azimuth Elevation for Ohio Ground Station",
    ephemeris={
        "azEl": {
            "groundStation": "Ohio 1",
            "data": {
                "azElData": {
                    "angleUnit": "DEGREE_ANGLE",
                    "azElSegmentList": [
                        {
                            "referenceEpoch": "2024-03-15T10:00:00Z",
                            "validTimeRange": {
                                "startTime": "2024-03-15T10:00:00Z",
                                "endTime": "2024-03-15T10:15:00Z",
                            },
                            "azElList": [
                                {"dt": 0.0, "az": 45.0, "el": 10.0},
                                {"dt": 180.0, "az": 50.0, "el": 15.0},
                                {"dt": 360.0, "az": 55.0, "el": 20.0},
                                {"dt": 540.0, "az": 60.0, "el": 25.0},
                                {"dt": 720.0, "az": 65.0, "el": 30.0},
                                {"dt": 900.0, "az": 70.0, "el": 35.0},
                            ],
                        }
                    ],
                }
            },
        }
    },
)

print(f"Created ephemeris with ID: {azimuth_elevation_ephemeris['ephemerisId']}")

```

In this example:

- The azimuth elevation data is associated with the "Ohio 1" ground station
- Angles are specified in degrees
- The segment covers a 15-minute period
- The `dt` values are atomic seconds offset from the reference epoch
- Six azimuth/elevation pairs are provided (minimum is 5)

## Example: Upload azimuth elevation data from S3

For larger datasets, you can upload azimuth elevation data from an S3 bucket:

```
import boto3
import json

# Create AWS clients
s3_client = boto3.client("s3")
ground_station_client = boto3.client("groundstation")

# Define S3 bucket and key
bucket_name = "azimuth-elevation-bucket"
object_key = "singapore-azimuth-elevation.json"

# Create sample azimuth elevation data
azimuth_elevation_data = {
    "angleUnit": "DEGREE_ANGLE",
    "azElSegmentList": [
        {
            "referenceEpoch": "2024-03-15T10:00:00Z",
            "validTimeRange": {
                "startTime": "2024-03-15T10:00:00Z",
                "endTime": "2024-03-15T10:15:00Z",
            },
            "azElList": [
                {"dt": 0.0, "az": 45.0, "el": 10.0},
                {"dt": 180.0, "az": 50.0, "el": 15.0},
                {"dt": 360.0, "az": 55.0, "el": 20.0},
                {"dt": 540.0, "az": 60.0, "el": 25.0},
                {"dt": 720.0, "az": 65.0, "el": 30.0},
                {"dt": 900.0, "az": 70.0, "el": 35.0},
            ],
        },
        {
            "referenceEpoch": "2024-03-15T10:15:00Z",
            "validTimeRange": {
                "startTime": "2024-03-15T10:15:00Z",
                "endTime": "2024-03-15T10:30:00Z",
            },
            "azElList": [
                {"dt": 0.0, "az": 70.0, "el": 35.0},
                {"dt": 180.0, "az": 75.0, "el": 40.0},
                {"dt": 360.0, "az": 80.0, "el": 45.0},
                {"dt": 540.0, "az": 85.0, "el": 50.0},
                {"dt": 720.0, "az": 90.0, "el": 55.0},
                {"dt": 900.0, "az": 95.0, "el": 50.0},
            ],
        },
    ],
}

# Upload sample data to S3
print(f"Uploading azimuth elevation data to s3://{bucket_name}/{object_key}")

s3_client.put_object(
    Bucket=bucket_name,
    Key=object_key,
    Body=json.dumps(azimuth_elevation_data, indent=2),
    ContentType="application/json",
)
print("Sample data uploaded successfully to S3")

# Create azimuth elevation ephemeris from S3
print("Creating azimuth elevation ephemeris from S3...")

s3_azimuth_elevation_ephemeris = ground_station_client.create_ephemeris(
    name="Large Azimuth Elevation Dataset",
    ephemeris={
        "azEl": {
            "groundStation": "Singapore 1",
            "data": {"s3Object": {"bucket": bucket_name, "key": object_key}},
        }
    },
)

print(f"Created ephemeris with ID: {s3_azimuth_elevation_ephemeris['ephemerisId']}")

```

The S3 object should contain a JSON structure with the azimuth elevation data in the same format
as shown in the direct upload example.

## Reserving contacts with azimuth elevation ephemeris

When using an azimuth elevation ephemeris to reserve a contact, the process differs from TLE and OEM ephemeris:

1. Create the azimuth elevation ephemeris using [CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md")
2. Wait for the ephemeris to reach `ENABLED` status
3. Reserve the contact using [ReserveContact](../APIReference/API_ReserveContact.md "../APIReference/API_ReserveContact.md") with tracking overrides

Example of reserving a contact with azimuth elevation ephemeris:

```
import boto3
from datetime import datetime
import time

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# First, create an azimuth elevation ephemeris
print("Creating azimuth elevation ephemeris...")

create_ephemeris_response = ground_station_client.create_ephemeris(
    name="Azimuth Elevation for Contact Reservation",
    ephemeris={
        "azEl": {
            "groundStation": "Ohio 1",
            "data": {
                "azElData": {
                    "angleUnit": "DEGREE_ANGLE",
                    "azElSegmentList": [
                        {
                            "referenceEpoch": "2024-03-15T10:00:00Z",
                            "validTimeRange": {
                                "startTime": "2024-03-15T10:00:00Z",
                                "endTime": "2024-03-15T10:15:00Z",
                            },
                            "azElList": [
                                {"dt": 0.0, "az": 45.0, "el": 10.0},
                                {"dt": 180.0, "az": 50.0, "el": 15.0},
                                {"dt": 360.0, "az": 55.0, "el": 20.0},
                                {"dt": 540.0, "az": 60.0, "el": 25.0},
                                {"dt": 720.0, "az": 65.0, "el": 30.0},
                                {"dt": 900.0, "az": 70.0, "el": 35.0},
                            ],
                        }
                    ],
                }
            },
        }
    },
)

ephemeris_id = create_ephemeris_response["ephemerisId"]
print(f"Created ephemeris with ID: {ephemeris_id}")

# Wait for ephemeris to become ENABLED
print("Waiting for ephemeris to become ENABLED...")

while True:
    status = ground_station_client.describe_ephemeris(ephemerisId=ephemeris_id)[
        "status"
    ]
    if status == "ENABLED":
        print("Ephemeris is ENABLED")
        break
    elif status in ["INVALID", "ERROR"]:
        raise RuntimeError(f"Ephemeris failed: {status}")
    time.sleep(5)

# Reserve contact with azimuth elevation ephemeris
print("Reserving contact...")

contact = ground_station_client.reserve_contact(
    # Note: satelliteArn is omitted when using azimuth elevation ephemeris
    missionProfileArn="arn:aws:groundstation:us-east-2:111122223333:mission-profile/example-mission-profile",
    groundStation="Ohio 1",
    startTime=datetime(2024, 3, 15, 10, 0, 0),
    endTime=datetime(2024, 3, 15, 10, 15, 0),
    trackingOverrides={"programTrackSettings": {"azEl": {"ephemerisId": ephemeris_id}}},
)

print(f"Reserved contact with ID: {contact['contactId']}")

```

###### Note

The `satelliteArn` parameter may be omitted when reserving a contact with azimuth elevation ephemeris.
The antenna will follow the specified azimuth and elevation angles during the contact.

## Listing available contacts

When using azimuth elevation ephemeris, the [ListContacts](../APIReference/API_ListContacts.md "../APIReference/API_ListContacts.md") API requires specific parameters:

- The `satelliteArn` parameter may be omitted from the request
- You must provide an `ephemeris` parameter with the azimuth elevation ephemeris ID to specify which ephemeris to use
- Available contact windows show when the provided azimuth and elevation angles are above the [site mask](locations.md "locations.md") of the requested ground station
- You must still provide `groundStation` and `missionProfileArn`

Example of creating an azimuth elevation ephemeris and listing available contacts with it:

```
import boto3
from datetime import datetime, timezone
import time

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# Step 1: Create azimuth elevation ephemeris
print("Creating azimuth elevation ephemeris...")
ephemeris_response = ground_station_client.create_ephemeris(
    name="Stockholm AzEl Ephemeris",
    ephemeris={
        "azEl": {
            "groundStation": "Stockholm 1",
            "data": {
                "azElData": {
                    "angleUnit": "DEGREE_ANGLE",
                    "azElSegmentList": [
                        {
                            "referenceEpoch": "2024-04-01T12:00:00Z",
                            "validTimeRange": {
                                "startTime": "2024-04-01T12:00:00Z",
                                "endTime": "2024-04-01T12:30:00Z",
                            },
                            "azElList": [
                                {"dt": 0.0, "az": 30.0, "el": 15.0},
                                {"dt": 360.0, "az": 45.0, "el": 30.0},
                                {"dt": 720.0, "az": 60.0, "el": 45.0},
                                {"dt": 1080.0, "az": 75.0, "el": 35.0},
                                {"dt": 1440.0, "az": 90.0, "el": 20.0},
                                {"dt": 1800.0, "az": 105.0, "el": 10.0},
                            ],
                        }
                    ],
                }
            },
        }
    },
)

ephemeris_id = ephemeris_response["ephemerisId"]
print(f"Created ephemeris: {ephemeris_id}")

# Step 2: Wait for ephemeris to become ENABLED
print("Waiting for ephemeris to become ENABLED...")
while True:
    describe_response = ground_station_client.describe_ephemeris(
        ephemerisId=ephemeris_id
    )
    status = describe_response["status"]

    if status == "ENABLED":
        print("Ephemeris is ENABLED")
        break
    elif status in ["INVALID", "ERROR"]:
        # Check for validation errors
        if "invalidReason" in describe_response:
            print(f"Ephemeris validation failed: {describe_response['invalidReason']}")
        raise RuntimeError(f"Ephemeris failed with status: {status}")

    print(f"Current status: {status}, waiting...")
    time.sleep(5)

# Step 3: List available contacts using the azimuth elevation ephemeris
print("Listing available contacts with azimuth elevation ephemeris...")

# Convert epoch timestamps to datetime objects
start_time = datetime.fromtimestamp(1760710513, tz=timezone.utc)
end_time = datetime.fromtimestamp(1760883313, tz=timezone.utc)

contacts_response = ground_station_client.list_contacts(
    startTime=start_time,
    endTime=end_time,
    groundStation="Stockholm 1",
    statusList=["AVAILABLE"],
    ephemeris={"azEl": {"id": ephemeris_id}},
    # satelliteArn is optional
    satelliteArn="arn:aws:groundstation::111122223333:satellite/a88611b0-f755-404e-b60d-57d8aEXAMPLE",
    missionProfileArn="arn:aws:groundstation:eu-north-1:111122223333:mission-profile/966b72f6-6d82-4e7e-b072-f8240EXAMPLE",
)

# Process the results
if contacts_response["contactList"]:
    print(f"Found {len(contacts_response['contactList'])} available contacts:")
    for contact in contacts_response["contactList"]:
        print(f"  - Contact from {contact['startTime']} to {contact['endTime']}")
        print(
            f"    Max elevation: {contact.get('maximumElevation', {}).get('value', 'N/A')}°"
        )
else:
    print("No available contacts found for the specified azimuth elevation ephemeris")

```

###### Note

The `ephemeris` parameter with the azimuth elevation ID must be provided when listing contacts
to specify which azimuth elevation ephemeris should be used for determining contact windows. If the
`satelliteArn` is included, it will be associated with the contact data, but the azimuth
elevation ephemeris will be used for antenna pointing rather than performing ephemeris priority resolution.
