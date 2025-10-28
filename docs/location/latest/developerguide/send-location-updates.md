# Update your tracker with a device

position

To track your devices, you can post device position updates to your tracker. You
can later retrieve these device positions or the device position history from your
tracker resource.

Each position update must include the device ID, a timestamp , and a position. You
may optionally include other metadata, including accuracy and up to 3 key-value
pairs for your own use.

If your tracker is linked to one or more geofence collections, updates will be
evaluated against those geofences (following the filtering rules that you specified
for the tracker). If a device breaches a geofenced area (by moving from inside the
area to outside, or vice versa), you will receive events in EventBridge. These
`ENTER` or `EXIT` events include the position update
details, including the device ID, the timestamp, and any associated metadata.

###### Note

For more information about position filtering, see [Create a tracker](start-create-tracker.md "start-create-tracker.md").

For more information about geofence events, see [React to Amazon Location Service events with Amazon EventBridge](location-events.md "location-events.md").

Use either of these methods to send device updates:

- [Send MQTT
  updates](tracking-using-mqtt.md "tracking-using-mqtt.md") to an AWS IoT Core resource and link it to your
  tracker resource.
- Send location updates using the Amazon Location Trackers API, by using the
  AWS CLI, or the Amazon Location APIs. You can use the [AWS SDKs](dev-sdks.md "dev-sdks.md") to call the APIs from
  your iOS or Android application.

API
**To send a position update using the Amazon Location
APIs**

Use the `BatchUpdateDevicePosition` operation from the
Amazon Location Trackers APIs.

The following example uses an API request to post a device position
update for `ExampleDevice` to a tracker
`ExampleTracker`.

```
POST /tracking/v0/trackers/`ExampleTracker`/positions
Content-type: application/json
{
 "Updates": [
    {
    "DeviceId": "1",
    "Position": [
   -123.12245146162303, 49.27521118043802
    ],
    "SampleTime": "2022-10-24T19:09:07.327Z",
     "PositionProperties": {
            "name" : "device1"
         },
         "Accuracy": {
            "Horizontal": 10
         }
    },

    {
    "DeviceId": "2",
    "Position": [
   -123.1230104928471, 49.27752402723152
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    },
    {
    "DeviceId": "3",
    "Position": [
    -123.12325592118916, 49.27340530543111
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    },
    {
    "DeviceId": "4",
    "Position": [
    -123.11958813096311, 49.27774641063121
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    },
    {
    "DeviceId": "5",
    "Position": [
    -123.1277418058896, 49.2765989015285
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    },
    {
    "DeviceId": "6",
    "Position": [
   -123.11964267059481, 49.274188155916534
    ],
    "SampleTime": "2022-10-02T19:09:07.327Z"
    }
    ]
}
```

AWS CLI
**To send a position update using AWS CLI
commands**

Use the `batch-update-device-position` command.

The following example uses an AWS CLI to post a device position update
for `ExampleDevice-1` and
`ExampleDevice-2` to a tracker
`ExampleTracker`.

```
aws location batch-update-device-position \
--tracker-name ExampleTracker \
--updates '[{"DeviceId":"ExampleDevice-1","Position":[-123.123,47.123],"SampleTime":"2021-11-30T21:47:25.149Z"},{"DeviceId":"ExampleDevice-2","Position":[-123.123,47.123],"SampleTime":"2021-11-30T21:47:25.149Z","Accuracy":{"Horizontal":10.30},"PositionProperties":{"field1":"value1","field2":"value2"}}]'
```
