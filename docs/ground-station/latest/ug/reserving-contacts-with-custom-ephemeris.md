# Reserve contacts with custom ephemeris

## Overview

When using custom ephemeris (TLE, OEM, or azimuth elevation), you can reserve contacts using the
[ReserveContact](../APIReference/API_ReserveContact.md "../APIReference/API_ReserveContact.md") API.
This section describes two common workflows for reserving contacts and important considerations for ensuring successful contact scheduling.

AWS Ground Station antennas are shared resources among multiple customers. This means that even if a contact
window appears available when you list contacts, another customer might reserve it before you do.
Therefore, it's crucial to verify that your contact reaches the `SCHEDULED` state
after reservation and to implement proper monitoring for contact state changes.

###### Important

For azimuth elevation ephemeris, the `satelliteArn` parameter may be omitted
from the `ReserveContact` request, and you must provide `trackingOverrides`
with the ephemeris ID. For TLE and OEM ephemeris, you still need to provide the `satelliteArn`.

## Contact reservation workflows

There are two primary workflows for reserving contacts with custom ephemeris:

1. _List-then-reserve workflow:_ First list available contact windows using
   [ListContacts](../APIReference/API_ListContacts.md "../APIReference/API_ListContacts.md"),
   then select and reserve a specific window. This approach is useful when you want to see all available
   opportunities before making a selection.
2. _Direct reservation workflow:_ Directly reserve a contact for a specific
   time window without first listing available contacts. This approach is useful when you already know
   your desired contact time or are working with predetermined schedules.

Both workflows are valid and the choice depends on your operational requirements. The following
sections provide examples of each approach.

## Workflow 1: List available contacts then reserve

This workflow first queries for available contact windows, then reserves a specific window.
This is useful when you want to see all available opportunities before making a selection.

### Example: List and reserve with azimuth elevation ephemeris

```
import boto3
from datetime import datetime, timezone
import time

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# Create azimuth elevation ephemeris
print("Creating azimuth elevation ephemeris...")
ephemeris_response = ground_station_client.create_ephemeris(
    name="AzEl Ephemeris for Contact",
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

ephemeris_id = ephemeris_response["ephemerisId"]
print(f"Created ephemeris: {ephemeris_id}")

# Wait for ephemeris to become ENABLED
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

# List available contacts
print("Listing available contacts...")
contacts = ground_station_client.list_contacts(
    # Note: satelliteArn is omitted for azimuth elevation ephemeris
    groundStation="Ohio 1",
    missionProfileArn="arn:aws:groundstation:us-east-2:111122223333:mission-profile/example-profile",
    startTime=datetime(2024, 3, 15, 10, 0, 0, tzinfo=timezone.utc),
    endTime=datetime(2024, 3, 15, 10, 15, 0, tzinfo=timezone.utc),
    statusList=["AVAILABLE"],
    ephemeris={"azEl": {"id": ephemeris_id}},
)

if contacts["contactList"]:
    # Reserve the first available contact
    contact = contacts["contactList"][0]
    print(f"Reserving contact from {contact['startTime']} to {contact['endTime']}...")

    reservation = ground_station_client.reserve_contact(
        # Note: satelliteArn is omitted when using azimuth elevation ephemeris
        missionProfileArn="arn:aws:groundstation:us-east-2:111122223333:mission-profile/example-profile",
        groundStation="Ohio 1",
        startTime=contact["startTime"],
        endTime=contact["endTime"],
        trackingOverrides={
            "programTrackSettings": {"azEl": {"ephemerisId": ephemeris_id}}
        },
    )

    print(f"Reserved contact: {reservation['contactId']}")
else:
    print("No available contacts found")

```

### Example: List and reserve with TLE ephemeris

```
import boto3
from datetime import datetime, timedelta, timezone
import time

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

satellite_id = "12345678-1234-1234-1234-123456789012"
satellite_arn = f"arn:aws:groundstation::111122223333:satellite/{satellite_id}"

# Create TLE ephemeris
print("Creating TLE ephemeris...")
ephemeris_response = ground_station_client.create_ephemeris(
    name="TLE Ephemeris for Contact",
    satelliteId=satellite_id,
    enabled=True,
    expirationTime=datetime.now(timezone.utc) + timedelta(days=7),
    priority=1,  # Higher priority than default ephemeris
    ephemeris={
        "tle": {
            "tleData": [
                {
                    "tleLine1": "1 25994U 99068A   24075.54719794  .00000075  00000-0  26688-4 0  9997",
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

ephemeris_id = ephemeris_response["ephemerisId"]
print(f"Created ephemeris: {ephemeris_id}")

# Wait for ephemeris to become ENABLED
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

# List available contacts
print("Listing available contacts...")
start_time = datetime.now(timezone.utc) + timedelta(hours=1)
end_time = start_time + timedelta(days=1)

contacts = ground_station_client.list_contacts(
    satelliteArn=satellite_arn,  # Required for TLE/OEM ephemeris
    groundStation="Hawaii 1",
    missionProfileArn="arn:aws:groundstation:us-west-2:111122223333:mission-profile/example-profile",
    startTime=start_time,
    endTime=end_time,
    statusList=["AVAILABLE"],
)

if contacts["contactList"]:
    # Reserve the first available contact
    contact = contacts["contactList"][0]
    print(f"Reserving contact from {contact['startTime']} to {contact['endTime']}...")

    reservation = ground_station_client.reserve_contact(
        satelliteArn=satellite_arn,  # Required for TLE/OEM ephemeris
        missionProfileArn="arn:aws:groundstation:us-west-2:111122223333:mission-profile/example-profile",
        groundStation="Hawaii 1",
        startTime=contact["startTime"],
        endTime=contact["endTime"],
        # Note: trackingOverrides is optional for TLE/OEM
        # The system will use the highest priority ephemeris automatically
    )

    print(f"Reserved contact: {reservation['contactId']}")
else:
    print("No available contacts found")

```

## Workflow 2: Direct contact reservation

This workflow directly reserves a contact without first listing available windows. This approach
is useful when you already know your desired contact time or are implementing automated scheduling.

### Example: Direct reservation with azimuth elevation ephemeris

```
import boto3
from datetime import datetime, timezone
import time

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# Define contact window
contact_start = datetime(2024, 3, 20, 14, 0, 0, tzinfo=timezone.utc)
contact_end = datetime(2024, 3, 20, 14, 15, 0, tzinfo=timezone.utc)

# Create azimuth elevation ephemeris for the specific contact time
print("Creating azimuth elevation ephemeris...")
ephemeris_response = ground_station_client.create_ephemeris(
    name="Direct Contact AzEl Ephemeris",
    ephemeris={
        "azEl": {
            "groundStation": "Ohio 1",
            "data": {
                "azElData": {
                    "angleUnit": "DEGREE_ANGLE",
                    "azElSegmentList": [
                        {
                            "referenceEpoch": contact_start.isoformat(),
                            "validTimeRange": {
                                "startTime": contact_start.isoformat(),
                                "endTime": contact_end.isoformat(),
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

ephemeris_id = ephemeris_response["ephemerisId"]
print(f"Created ephemeris: {ephemeris_id}")

# Wait for ephemeris to become ENABLED
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

# Directly reserve the contact
print(f"Reserving contact from {contact_start} to {contact_end}...")

reservation = ground_station_client.reserve_contact(
    # Note: satelliteArn is omitted for azimuth elevation
    missionProfileArn="arn:aws:groundstation:us-east-2:111122223333:mission-profile/example-profile",
    groundStation="Ohio 1",
    startTime=contact_start,
    endTime=contact_end,
    trackingOverrides={"programTrackSettings": {"azEl": {"ephemerisId": ephemeris_id}}},
)

print(f"Reserved contact: {reservation['contactId']}")

```

### Example: Direct reservation with TLE ephemeris

```
import boto3
from datetime import datetime, timedelta, timezone
import time

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

satellite_id = "12345678-1234-1234-1234-123456789012"
satellite_arn = f"arn:aws:groundstation::111122223333:satellite/{satellite_id}"

# Define contact window (based on predicted pass)
contact_start = datetime(2024, 3, 21, 10, 30, 0, tzinfo=timezone.utc)
contact_end = datetime(2024, 3, 21, 10, 42, 0, tzinfo=timezone.utc)

# Create TLE ephemeris
print("Creating TLE ephemeris...")
ephemeris_response = ground_station_client.create_ephemeris(
    name="Direct Contact TLE Ephemeris",
    satelliteId=satellite_id,
    enabled=True,
    expirationTime=contact_end + timedelta(days=1),
    priority=1,
    ephemeris={
        "tle": {
            "tleData": [
                {
                    "tleLine1": "1 25994U 99068A   24080.50000000  .00000075  00000-0  26688-4 0  9999",
                    "tleLine2": "2 25994  98.2007  35.6589 0001234  89.2782  18.9934 14.57114995112000",
                    "validTimeRange": {
                        "startTime": (contact_start - timedelta(hours=1)).isoformat(),
                        "endTime": (contact_end + timedelta(hours=1)).isoformat(),
                    },
                }
            ]
        }
    },
)

ephemeris_id = ephemeris_response["ephemerisId"]
print(f"Created ephemeris: {ephemeris_id}")

# Wait for ephemeris to become ENABLED
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

# Directly reserve the contact
print(f"Reserving contact from {contact_start} to {contact_end}...")

reservation = ground_station_client.reserve_contact(
    satelliteArn=satellite_arn,  # Required for TLE ephemeris
    missionProfileArn="arn:aws:groundstation:us-west-2:111122223333:mission-profile/example-profile",
    groundStation="Hawaii 1",
    startTime=contact_start,
    endTime=contact_end,
    # Note: trackingOverrides is optional for TLE
    # The system will use the highest priority ephemeris automatically
)

print(f"Reserved contact: {reservation['contactId']}")

```

## Monitoring contact state changes

After reserving a contact, it's important to monitor its state to ensure it successfully transitions
to `SCHEDULED` and to be notified of any issues. AWS Ground Station emits events to
Amazon EventBridge for all contact state changes.

Contact states follow this lifecycle:

- `SCHEDULING` - The contact is being processed for scheduling
- `SCHEDULED` - The contact was successfully scheduled and will execute
- `FAILED_TO_SCHEDULE` - The contact could not be scheduled (terminal state)

For more information on contact states and lifecycle, see
[Understand contact lifecycle](contacts.md "contacts.md").

### Implementing contact state monitoring with EventBridge

To monitor contact state changes in real-time, you can set up an Amazon EventBridge rule that triggers
a Lambda function whenever a Ground Station contact changes state. This approach is more efficient and
scalable than polling the contact status.

#### Implementation steps

1. Create a Lambda function to process contact state change events
2. Create an EventBridge rule that matches Ground Station contact state change events
3. Add the Lambda function as a target for the rule

#### Example Lambda function handler

For a complete example of a Lambda function that processes contact state change events, see the
`GroundStationCloudWatchEventHandlerLambda` resource in the
`AquaSnppJpssTerraDigIF.yml` AWS CloudFormation template. This template is available in the
AWS Ground Station customer onboarding Amazon S3 bucket. For instructions on accessing this template, see the
[Putting it together](examples.md#examples.pbs-dataflow-endpoint.putting-it-together "examples.md#examples.pbs-dataflow-endpoint.putting-it-together") section of the dataflow endpoint example.

#### EventBridge rule configuration

The EventBridge rule should use the following event pattern to match all Ground Station contact state changes:

```
{
  "source": ["aws.groundstation"],
  "detail-type": ["Ground Station Contact State Change"]
}
```

To filter for specific states only (e.g., failures), you can add a detail filter:

```
{
  "source": ["aws.groundstation"],
  "detail-type": ["Ground Station Contact State Change"],
  "detail": {
    "contactStatus": [
      "FAILED_TO_SCHEDULE",
      "FAILED",
      "AWS_FAILED",
      "AWS_CANCELLED"
    ]
  }
}
```

For detailed instructions on creating EventBridge rules with Lambda targets, see
[Creating rules that react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md")
in the Amazon EventBridge User Guide.

### Setting up EventBridge rules for automation

You can create EventBridge rules to automatically respond to contact state changes. For example:

- Send notifications when a contact fails to schedule
- Trigger Lambda functions to prepare resources when a contact enters `PREPASS`
- Log contact completions for auditing purposes

For detailed information on setting up EventBridge rules for AWS Ground Station events, see
[Automate AWS Ground Station with
Events](monitoring.md "monitoring.md").

## Best practices and considerations

### Handling scheduling conflicts

Since AWS Ground Station antennas are shared resources, a contact window that appears available in
`ListContacts` might be reserved by another customer before you can reserve it.
To handle this:

1. Always check the contact status after reservation
2. Implement retry logic with alternative time windows
3. Consider reserving contacts well in advance when possible
4. Use EventBridge events to monitor for `FAILED_TO_SCHEDULE` states

### Ephemeris validation timing

Remember that ephemeris must be in `ENABLED` state before you can use it to
reserve contacts. The validation process typically takes a few seconds to a few minutes depending
on the ephemeris type and size. Always verify the ephemeris status before attempting to reserve contacts.

### Contact timing considerations

When using custom ephemeris:

- Ensure your ephemeris covers the entire contact duration
- For azimuth elevation ephemeris, verify that the angles keep the antenna above the [site mask](locations.md "locations.md") throughout the contact
- Consider ephemeris expiration times when scheduling future contacts

### API differences by ephemeris type

The `ReserveContact` API behaves differently depending on the ephemeris type:

| Ephemeris Type    | satelliteArn Required | trackingOverrides Required |
| ----------------- | --------------------- | -------------------------- |
| TLE               | Yes                   | No (optional)              |
| OEM               | Yes                   | No (optional)              |
| Azimuth Elevation | No (optional)         | Yes                        |
