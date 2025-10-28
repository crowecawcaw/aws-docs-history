# Get the current ephemeris for a satellite

The current ephemeris in use by AWS Ground Station for a specific satellite can be retrieved by calling the
[GetSatellite](../APIReference/API_GetSatellite.md "../APIReference/API_GetSatellite.md") or [ListSatellites](../APIReference/API_ListSatellites.md "../APIReference/API_ListSatellites.md") actions. Both of these methods will return
metadata for the ephemeris currently in use. This ephemeris metadata is different for custom ephemerides uploaded
to AWS Ground Station and for default ephemerides.

Default Ephemerides will only include `source` and `epoch` fields. The
`epoch` is the [epoch](<https://en.wikipedia.org/wiki/Epoch_(astronomy)> "https://en.wikipedia.org/wiki/Epoch_(astronomy)") of the
[two-line element set](https://en.wikipedia.org/wiki/Two-line_element_set "https://en.wikipedia.org/wiki/Two-line_element_set") that was pulled from
[Space-Track](https://www.space-track.org/ "https://www.space-track.org/"), and it is currently being used for computing the trajectory of the satellite.

A custom ephemeris will have a `source` value of `"CUSTOMER_PROVIDED"` and will
include a unique identifier in the `ephemerisId` field. This unique identifier can be used to query
for the ephemeris via the [DescribeEphemeris](../APIReference/API_DescribeEphemeris.md "../APIReference/API_DescribeEphemeris.md") action. An optional `name` field
will be returned if the ephemeris was assigned a name during upload to AWS Ground Station via the
[CreateEphemeris](../APIReference/API_CreateEphemeris.md "../APIReference/API_CreateEphemeris.md") action.

It is important to note that ephemerides are updated dynamically by AWS Ground Station so the returned data is only
a snapshot of the ephemeris being used at the time of the call to the API.

## Example `GetSatellite` return for a satellite using a default ephemeris

```
{
    "satelliteId": "e1cfe0c7-67f9-4d98-bad2-06dbfc2d14a2",
    "satelliteArn": "arn:aws:groundstation::111122223333:satellite/e1cfe0c7-67f9-4d98-bad2-06dbfc2d14a2",
    "noradSatelliteID": 12345,
    "groundStations": [
        "Example Ground Station 1",
        "Example Ground Station 2"
    ],
    "currentEphemeris": {
        "source": "SPACE_TRACK",
        "epoch": 8888888888
    }
}
```

## Example `GetSatellite` for a satellite using a custom ephemeris

```
{
      "satelliteId": "e1cfe0c7-67f9-4d98-bad2-06dbfc2d14a2",
      "satelliteArn": "arn:aws:groundstation::111122223333:satellite/e1cfe0c7-67f9-4d98-bad2-06dbfc2d14a2",
      "noradSatelliteID": 12345,
      "groundStations": [
          "Example Ground Station 1",
          "Example Ground Station 2"
      ],
      "currentEphemeris": {
          "source": "CUSTOMER_PROVIDED",
          "ephemerisId": "e1cfe0c7-67f9-4d98-bad2-06dbfc2d14a2",
          "name": "My Ephemeris"
      }
  }
```
