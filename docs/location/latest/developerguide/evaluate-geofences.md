# Evaluate device positions against

geofences

There are two ways to evaluate positions against geofences to generate geofence
events:

- You can link Trackers and Geofence Collections. For more information, see
  the section: [Link a tracker to a geofence collection](associate-consumer.md "associate-consumer.md").
- You can make a direct request to the geofence collection resource to
  evaluate one or more positions.
  If you also want to track your device location history or display locations on a
  map, link the tracker with a geofence collection. Alternatively, you may not want to
  evaluate all location updates, or you don't intend to store location data in a
  tracker resource. If either of these is the case, you can make a direct request to
  the geofence collection and evaluate one or more device positions against its
  geofences.

Evaluating device positions against geofences generates events. You can react to
these events and route them to other AWS services. For more information about
actions that you can take when receiving geofence events, see [Reacting to Amazon Location Service events with Amazon
EventBridge](location-events.md "location-events.md").

An Amazon Location event includes the attributes of the device position update that
generates it, including the time, position, accuracy, and key-value metadata, and
some attributes of the geofence that is entered or exited. For more information
about the data included in a geofence event, see [Amazon EventBridge event examples for Amazon Location Service](location-events.md#example-event "location-events.md#example-event").

The following examples use the AWS CLI, or the Amazon Location APIs.

API
**To evaluate device positions against the
position of geofences using the Amazon Location APIs**

Use the `BatchEvaluateGeofences` operation from the
Amazon Location Geofences APIs.

The following example uses an API request to evaluate the position of
device `ExampleDevice` to an associated
geofence collection
`ExampleGeofenceCollection`. Replace these
values with your own geofence and device IDs.

```
POST /geofencing/v0/collections/`ExampleGeofenceCollection`/positions HTTP/1.1
Content-type: application/json

{
   "DevicePositionUpdates": [
      {
         "DeviceId": "`ExampleDevice`",
         "Position": `[-123.123, 47.123]`,
         "SampleTime": "2021-11-30T21:47:25.149Z",
         "Accuracy": {
            "Horizontal": 10.30
         },
         "PositionProperties": {
            "field1": "value1",
            "field2": "value2"
         }
      }
   ]
}
```

AWS CLI
**To evaluate device positions against the
position of geofences using AWS CLI commands**

Use the `batch-evaluate-geofences` command.

The following example uses an AWS CLI to evaluate the position of
`ExampleDevice` against an associated
geofence collection
`ExampleGeofenceCollection`. Replace these
values with your own geofence and device IDs.

```
aws location \
    batch-evaluate-geofences \
        --collection-name `ExampleGeofenceCollection` \
        --device-position-updates '[{"DeviceId":"`ExampleDevice`","Position":[-123.123,47.123],"SampleTime":"2021-11-30T21:47:25.149Z","Accuracy":{"Horizontal":10.30},"PositionProperties":{"field1":"value1","field2":"value2"}}]'
```
