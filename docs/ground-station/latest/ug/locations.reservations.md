

# View ground station reservations
<a name="locations.reservations"></a>

 You can view reservations across antennas at a ground station by using the [ListGroundStationReservations](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStationReservations.html) API. Reservations represent time blocks on antennas, including your scheduled contacts. [AWS Ground Station Dedicated Antennas](dedicated-antennas.md) customers also see maintenance windows. 

 This information helps you understand antenna availability when planning contact schedules and provides visibility into what is happening on the antennas at a ground station. 

## Listing reservations
<a name="locations.reservations.listing"></a>

 To list reservations, call [ListGroundStationReservations](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStationReservations.html) with a ground station identifier and a time range. The API returns reservations across all antennas at the ground station within the specified time window. 

 The reservations you see depend on your access level: 
+  **Public AWS Ground Station customers** — You can see only your own contact reservations. Maintenance windows and contacts owned by other accounts are not included. 
+  **AWS Ground Station Dedicated Antennas customers** — You can see all reservations on your Dedicated Antennas, including maintenance windows and contacts scheduled by other accounts. Contact identifiers are only included for contacts that you own. For more information, see [AWS Ground Station Dedicated Antennas](dedicated-antennas.md). 

## Reservation types
<a name="locations.reservations.types"></a>

Each reservation has a type that indicates what the antenna time is being used for:
+  **Contact** — A contact reservation represents antenna time reserved for satellite communication. The reservation start and end times reflect the full antenna reservation, including pre-pass and post-pass time, not just the satellite pass window. 
+  **Maintenance** — A maintenance reservation represents a time period when the antenna is unavailable due to maintenance. Maintenance reservations include a `maintenanceType` that indicates whether the maintenance was planned or unplanned. 

## Code example
<a name="locations.reservations.examples"></a>

 The following example lists reservations at a ground station for the next 7 days using the AWS SDK for Python (Boto3), including filtering by reservation type. 

```
import boto3
from datetime import datetime, timezone, timedelta

# Create AWS Ground Station client
ground_station_client = boto3.client("groundstation")

# The ground station ID to list reservations for
ground_station_id = "Ohio 1"

# Define the time range to query. Reservations include both your
# scheduled contacts and maintenance windows at the ground station.
start_time = datetime.now(timezone.utc)
end_time = start_time + timedelta(days=7)

# List all reservations at a ground station for the next 7 days.
# You can filter by reservation type to see only contacts or
# only maintenance windows.
print(f"Listing reservations for ground station '{ground_station_id}'...")
print(f"Time range: {start_time} to {end_time}")

paginator = ground_station_client.get_paginator("list_ground_station_reservations")
page_iterator = paginator.paginate(
    groundStationId=ground_station_id,
    startTime=start_time,
    endTime=end_time,
    PaginationConfig={
        "MaxItems": 100,
        "PageSize": 20,
    },
)

for page in page_iterator:
    for reservation in page["reservationList"]:
        reservation_type = reservation["reservationType"]
        antenna_name = reservation["antennaName"]
        res_start = reservation["startTime"]
        res_end = reservation["endTime"]

        print(f"  Type: {reservation_type}")
        print(f"    Antenna: {antenna_name}")
        print(f"    Start: {res_start}")
        print(f"    End: {res_end}")

        details = reservation["reservationDetails"]
        if "contact" in details:
            contact_id = details["contact"].get("contactId", "N/A")
            print(f"    Contact ID: {contact_id}")
        elif "maintenance" in details:
            maintenance_type = details["maintenance"]["maintenanceType"]
            print(f"    Maintenance Type: {maintenance_type}")

        print()

# For Dedicated Antenna customers, you can also filter to show only maintenance windows
print("Listing only maintenance reservations...")

page_iterator = paginator.paginate(
    groundStationId=ground_station_id,
    startTime=start_time,
    endTime=end_time,
    reservationTypes=["MAINTENANCE"],
    PaginationConfig={
        "MaxItems": 100,
        "PageSize": 20,
    },
)

for page in page_iterator:
    for reservation in page["reservationList"]:
        maintenance_type = reservation["reservationDetails"]["maintenance"][
            "maintenanceType"
        ]
        print(
            f"  {maintenance_type} maintenance on {reservation['antennaName']}: "
            f"{reservation['startTime']} to {reservation['endTime']}"
        )
```