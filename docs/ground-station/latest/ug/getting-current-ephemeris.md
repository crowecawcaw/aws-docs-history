# Get the current ephemeris for a satellite

The current ephemeris in use by AWS Ground Station for a specific satellite can be retrieved by calling the
[GetSatellite](../APIReference/API_GetSatellite.md "../APIReference/API_GetSatellite.md") or [ListSatellites](../APIReference/API_ListSatellites.md "../APIReference/API_ListSatellites.md") actions. Both of these methods will return
metadata for the ephemeris currently in use. This ephemeris metadata is different for custom ephemerides uploaded
to AWS Ground Station and for default ephemerides.

###### Note

Azimuth elevation ephemerides are not associated with satellites and therefore are not returned
by [GetSatellite](../APIReference/API_GetSatellite.md "../APIReference/API_GetSatellite.md") or [ListSatellites](../APIReference/API_ListSatellites.md "../APIReference/API_ListSatellites.md"). To retrieve information
about azimuth elevation ephemerides, use the [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") API with the
specific ephemeris ID, or use [ListEphemerides](../APIReference/API_ListEphemerides.md "../APIReference/API_ListEphemerides.md") to see all available ephemerides
for your account.

Default Ephemerides will only include `source` and `epoch` fields. The
`epoch` is the [epoch](<https://en.wikipedia.org/wiki/Epoch_(astronomy)> "https://en.wikipedia.org/wiki/Epoch_(astronomy)") of the
[two-line element set](https://en.wikipedia.org/wiki/Two-line_element_set "https://en.wikipedia.org/wiki/Two-line_element_set") that was pulled from
[Space-Track](https://www.space-track.org/ "https://www.space-track.org/"), and it is currently being used for computing the trajectory of the satellite.

A custom ephemeris will have a `source` value of `CUSTOMER_PROVIDED` and will
include a unique identifier in the `ephemerisId` field. This unique identifier can be used to query
for the ephemeris via the [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") action. An optional `name` field
will be returned if the ephemeris was assigned a name during upload to AWS Ground Station via the
[CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md") action.

It is important to note that ephemerides are updated dynamically by AWS Ground Station so the returned data is only
a snapshot of the ephemeris being used at the time of the call to the API.

## Example [GetSatellite](../APIReference/API_GetSatellite.md "../APIReference/API_GetSatellite.md") return for a satellite using a default ephemeris

```
{
    "satelliteId": "e1cfe0c7-67f9-4d98-bad2-EXAMPLE",
    "satelliteArn": "arn:aws:groundstation::111122223333:satellite/e1cfe0c7-67f9-4d98-bad2-EXAMPLE",
    "noradSatelliteID": 25994,
    "groundStations": [
        "Ohio 1",
        "Oregon 1"
    ],
    "currentEphemeris": {
        "source": "SPACE_TRACK",
        "epoch": 1528245583.619
    }
}
```

## Example [GetSatellite](../APIReference/API_GetSatellite.md "../APIReference/API_GetSatellite.md") for a satellite using a custom ephemeris

```
{
      "satelliteId": "e1cfe0c7-67f9-4d98-bad2-EXAMPLE",
      "satelliteArn": "arn:aws:groundstation::111122223333:satellite/e1cfe0c7-67f9-4d98-bad2-EXAMPLE",
      "noradSatelliteID": 25994,
      "groundStations": [
            "Ohio 1",
            "Oregon 1"
      ],
      "currentEphemeris": {
          "source": "CUSTOMER_PROVIDED",
          "ephemerisId": "e1cfe0c7-67f9-4d98-bad2-EXAMPLE",
          "name": "My Ephemeris"
      }
  }
```

## Listing azimuth elevation ephemerides

Since azimuth elevation ephemerides are not associated with satellites, you need to use different
APIs to discover and retrieve information about them:

1. Use [ListEphemerides](../APIReference/API_ListEphemerides.md "../APIReference/API_ListEphemerides.md") to list all ephemerides in your account, including
   azimuth elevation ephemerides. You can filter by status and ephemeris type.
2. Use [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") with a specific ephemeris ID to get detailed
   information about an azimuth elevation ephemeris.
3. Use [DescribeContact](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md") with a specific contact ID to get detailed information about an ephemeris used for the contact.

Example [ListEphemerides](../APIReference/API_ListEphemerides.md "../APIReference/API_ListEphemerides.md") response including an azimuth elevation ephemeris:

```
{
    "ephemerides": [
        {
            "ephemerisId": "abc12345-6789-def0-1234-5678EXAMPLE",
            "ephemerisType": "AZ_EL",
            "name": "Azimuth Elevation for Ohio Ground Station",
            "status": "ENABLED",
            "creationTime": 1620254718.765
        },
        {
            "ephemerisId": "def45678-9012-abc3-4567-8901EXAMPLE",
            "ephemerisType": "TLE",
            "name": "TLE for Satellite 12345",
            "status": "ENABLED",
            "creationTime": 1620254700.123
        }
    ]
}
```

###### Note

In the [ListEphemerides](../APIReference/API_ListEphemerides.md "../APIReference/API_ListEphemerides.md") response, azimuth elevation ephemerides will have
a `groundStation` field instead of a `satelliteId` field,
making them easy to identify.
