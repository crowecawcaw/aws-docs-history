

# Get the current ephemeris for a satellite
<a name="getting-current-ephemeris"></a>

 The current ephemeris in use by AWS Ground Station for a specific satellite can be retrieved by calling the [GetSatellite](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetSatellite.html) or [ListSatellites](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListSatellites.html) actions. Both of these methods will return metadata for the ephemeris currently in use. This ephemeris metadata is different for custom ephemerides uploaded to AWS Ground Station and for default ephemerides. 

**Note**  
 Azimuth elevation ephemerides are not associated with satellites and therefore are not returned by [GetSatellite](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetSatellite.html) or [ListSatellites](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListSatellites.html). To retrieve information about azimuth elevation ephemerides, use the [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) API with the specific ephemeris ID, or use [ListEphemerides](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListEphemerides.html) to see all available ephemerides for your account. 

 Default Ephemerides will only include `source` and `epoch` fields. The `epoch` is the [epoch](https://en.wikipedia.org/wiki/Epoch_(astronomy)) of the [two-line element set](https://en.wikipedia.org/wiki/Two-line_element_set) that was pulled from [Space-Track](https://www.space-track.org/), and it is currently being used for computing the trajectory of the satellite. 

 A custom ephemeris will have a `source` value of `CUSTOMER_PROVIDED` and will include a unique identifier in the `ephemerisId` field. This unique identifier can be used to query for the ephemeris via the [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) action. An optional `name` field will be returned if the ephemeris was assigned a name during upload to AWS Ground Station via the [CreateEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEphemeris.html) action. 

 It is important to note that ephemerides are updated dynamically by AWS Ground Station so the returned data is only a snapshot of the ephemeris being used at the time of the call to the API. 

## Example [GetSatellite](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetSatellite.html) return for a satellite using a default ephemeris
<a name="w2aac28c23c13"></a>

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

## Example [GetSatellite](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetSatellite.html) for a satellite using a custom ephemeris
<a name="w2aac28c23c15"></a>

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
<a name="w2aac28c23c17"></a>

 Since azimuth elevation ephemerides are not associated with satellites, you need to use different APIs to discover and retrieve information about them: 

1. Use [ListEphemerides](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListEphemerides.html) to list all ephemerides in your account, including azimuth elevation ephemerides. You can filter by status and ephemeris type.

1. Use [DescribeEphemeris](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html) with a specific ephemeris ID to get detailed information about an azimuth elevation ephemeris.

1. Use [DescribeContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeContact.html) with a specific contact ID to get detailed information about an ephemeris used for the contact.

 Example [ListEphemerides](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListEphemerides.html) response including an azimuth elevation ephemeris: 

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

**Note**  
 In the [ListEphemerides](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListEphemerides.html) response, azimuth elevation ephemerides will have a `groundStation` field instead of a `satelliteId` field, making them easy to identify. 