# List your device positions

You can view a list device positions for a tracker using the AWS CLI, or the
Amazon Location APIs, with the ListDevicePositions API.
When you call the ListDevicePositions API, a list of the latest positions for all
devices associated with a given tracker is returned. By default this API returns 100 of the latest
device positions per page of results for a given tracker.
To only return devices within a specific region use the `FilterGeometry` parameter
to create a Bounding Polygon Query.
This way when you call ListDevicePositions, only devices inside the polygon will be returned.

###### Note

If you wish to encrypt your data using your own AWS KMS customer managed key, then the Bounding
Polygon Queries feature will be disabled by default. This is because by using
this feature, a representation of your device positions will not be encrypted
using your AWS KMS managed key. The exact device position, however; is still
encrypted using your managed key.

You can choose to opt-in to the Bounding Polygon Queries feature. This is done by setting the `KmsKeyEnableGeospatialQueries` parameter to true when creating or updating a Tracker.

API
Use the `ListDevicePositions` operation from the Amazon Location
Trackers APIs.

The following example is an API request to get a list of device positions in polygonal area,
using the optional parameter `FilterGeometry`. The example returns 3 device locations present in the area defined by the `Polygon` array.

```
POST /tracking/v0/trackers/`TrackerName`/list-positions HTTP/1.1
Content-type: application/json

{
   "FilterGeometry": {
        "Polygon": [
          [
            [
              -123.12003339442259,
              49.27425121147397
            ],
            [
              -123.1176984148229,
              49.277063620879744
            ],
            [
              -123.12389509145294,
              49.277954183760926
            ],
            [
              -123.12755921328647,
              49.27554025235713
            ],
            [
              -123.12330236586217,
              49.27211836076236
            ],
            [
              -123.12003339442259,
              49.27425121147397
            ]
          ]
        ]
    },
   "MaxResults": 3,
   "NextToken": "1234-5678-9012"
}
```

The following is an example response for `ListDevicePositions`:

```
{
    "Entries": [
        {
            "DeviceId": "1",
            "SampleTime": "2022-10-24T19:09:07.327Z",
            "Position": [
                -123.12245146162303,
                49.27521118043802
            ],
            "Accuracy": {
                "Horizontal": 10
            },
            "PositionProperties": {
                "name": "device1"
            }
        },
        {
            "DeviceId": "3",
            "SampleTime": "2022-10-02T19:09:07.327Z",
            "Position": [
                -123.12325592118916,
                49.27340530543111
            ]
        },
        {
            "DeviceId": "2",
            "SampleTime": "2022-10-02T19:09:07.327Z",
            "Position": [
                -123.1230104928471,
                49.27752402723152
            ]
        }
    ],
   "NextToken": "1234-5678-9012"
}
```

CLI
Use the `list-trackers` command.

The following example is an AWS CLI to get a list of devices in a polygonal area.

```
aws location list-device-positions TODO: add arguments add props for filter geo
```
