# React to Amazon Location Service events with Amazon EventBridge

Amazon EventBridge is a serverless event bus that efficiently connects applications together using
data from AWS services like Amazon Location. EventBridge receives events from Amazon Location and routes that
data to targets like AWS Lambda. You can set up routing rules to determine where to send your
data to build application architectures that react in real time.

Only geofence events (`ENTER` and `EXIT` events, as devices enter or
leave the geofenced areas) are sent to EventBridge by default. You can also enable all filtered
position update events for a tracker resource. For more information, see [Enable update events for a tracker](#enable-update-events "#enable-update-events").

For more information, see [the Events and
Event Patterns](../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md "../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md") in _the Amazon EventBridge User
Guide_.

###### Topics

- [Enable update events for a tracker](#enable-update-events "#enable-update-events")
- [Create event rules for Amazon Location](#create-event-rule "#create-event-rule")
- [Amazon EventBridge event examples for Amazon Location Service](#example-event "#example-event")

## Enable update events for a tracker

By default, Amazon Location sends only `ENTER` and `EXIT` geofence
events to EventBridge. You can enable all filtered position `UPDATE` events for a
tracker to be sent to EventBridge. You can do this when you [create](../APIReference/API_CreateTracker.md "../APIReference/API_CreateTracker.md") or [update](../APIReference/API_UpdateTracker.md "../APIReference/API_UpdateTracker.md") a tracker.

For example, to update an existing tracker using the AWS CLI, you can use the following
command (use the name of your tracker resource in place of
`MyTracker`).

```
aws location update-tracker --tracker-name `MyTracker` --event-bridge-enabled
```

To turn off position events for a tracker, you must use the API or the Amazon Location Service
console.

## Create event rules for Amazon Location

You can create [up to 300 rules per event
bus](../../../eventbridge/latest/userguide/eb-quota.md "../../../eventbridge/latest/userguide/eb-quota.md") in EventBridge to configure actions taken in response to an Amazon Location event.

For example, you can create a rule for geofence events where a push notification will
be sent when a phone is detected within a geofenced boundary.

**To create a rule for Amazon Location events**

Using the following values, [create an EventBridge rule](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md")
based on Amazon Location events:

- For **Rule type**, choose **Rule with an event
  pattern**.
- In the **Event pattern** box, add the following
  pattern:

```
{
  "source": ["aws.geo"],
  "detail-type": ["Location Geofence Event"]
}
```

To create a rule for tracker position updates, you can instead use the
following pattern:

```
{
  "source": ["aws.geo"],
  "detail-type": ["Location Device Position Event"]
}
```

You can optionally specify only `ENTER` or `EXIT` events
by adding a `detail` tag (if your rule is for tracker position
updates, there is only a single `EventType`, so there is no need to
filter on it):

```
{
  "source": ["aws.geo"],
  "detail-type": ["Location Geofence Event"],
  "detail": {
    "EventType": ["ENTER"]
  }
}
```

You can also optionally filter on properties of the position or
geofence:

```
{
  "source": ["aws.geo"],
  "detail-type": ["Location Geofence Event"],
  "detail": {
    "EventType": ["ENTER"],
    "GeofenceProperties": {
      "Type": "LoadingDock"
    },
    "PositionProperties": {
      "VehicleType": "Truck"
    }
  }
}
```

- For **Select targets**, choose the target action to take when
  an event is received from Amazon Location Service.

For example, use an Amazon Simple Notification Service (SNS) topic to send an email or text message
when an event occurs. You first need to create an Amazon SNS topic using the Amazon SNS
console. For more information, see [Using Amazon SNS for user
notifications](../../../sns/latest/dg/sns-user-notifications.md "../../../sns/latest/dg/sns-user-notifications.md").

###### Warning

It's best practice to confirm that the event rule was successfully applied or your
automated action may not initiate as expected. To verify your event rule, initiate
conditions for the event rule. For example, simulate a device entering a geofenced
area.

You can also capture all events from Amazon Location, by just excluding the
`detail-type` section. For example:

```
{
  "source": [
    "aws.geo"
  ]
}
```

###### Note

The same event may be delivered more than one time. You can use the event id to
de-duplicate the events that you receive.

## Amazon EventBridge event examples for Amazon Location Service

The following is an example of an event for entering a geofence initiated by calling
`BatchUpdateDevicePosition`.

```
{
  "version": "0",
  "id": "aa11aa22-33a-4a4a-aaa5-example",
  "detail-type": "Location Geofence Event",
  "source": "aws.geo",
  "account": "636103698109",
  "time": "2020-11-10T23:43:37Z",
  "region": "eu-west-1",
  "resources": [
    "arn:aws:geo:eu-west-1:0123456789101:geofence-collection/GeofenceEvents-GeofenceCollection_EXAMPLE",
    "arn:aws:geo:eu-west-1:0123456789101:tracker/Tracker_EXAMPLE"
  ],
  "detail": {
    "EventType": "ENTER",
    "GeofenceId": "polygon_14",
    "DeviceId": "Device1-EXAMPLE",
    "SampleTime": "2020-11-10T23:43:37.531Z",
    "Position": [
      -123.12390073297821,
      49.23433613216247
    ],
    "Accuracy": {
      "Horizontal": 15.3
    },
    "GeofenceProperties": {
      "ExampleKey1": "ExampleField1",
      "ExampleKey2": "ExampleField2"
    },
    "PositionProperties": {
      "ExampleKey1": "ExampleField1",
      "ExampleKey2": "ExampleField2"
    }
  }
}
```

The following is an example of an event for exiting a geofence initiated by calling
`BatchUpdateDevicePosition`.

```
{
  "version": "0",
  "id": "aa11aa22-33a-4a4a-aaa5-example",
  "detail-type": "Location Geofence Event",
  "source": "aws.geo",
  "account": "123456789012",
  "time": "2020-11-10T23:41:44Z",
  "region": "eu-west-1",
  "resources": [
    "arn:aws:geo:eu-west-1:0123456789101:geofence-collection/GeofenceEvents-GeofenceCollection_EXAMPLE",
    "arn:aws:geo:eu-west-1:0123456789101:tracker/Tracker_EXAMPLE"
  ],
  "detail": {
    "EventType": "EXIT",
    "GeofenceId": "polygon_10",
    "DeviceId": "Device1-EXAMPLE",
    "SampleTime": "2020-11-10T23:41:43.826Z",
    "Position": [
      -123.08569321875426,
      49.23766166742559
    ],
    "Accuracy": {
      "Horizontal": 15.3
    },
    "GeofenceProperties": {
      "ExampleKey1": "ExampleField1",
      "ExampleKey2": "ExampleField2"
    },
    "PositionProperties": {
      "ExampleKey1": "ExampleField1",
      "ExampleKey2": "ExampleField2"
    }
  }
}
```

The following is an example of an event for a position update, initiated by calling
`BatchUpdateDevicePosition`.

```
{
  "version": "0",
  "id": "aa11aa22-33a-4a4a-aaa5-example",
  "detail-type": "Location Device Position Event",
  "source": "aws.geo",
  "account": "123456789012",
  "time": "2020-11-10T23:41:44Z",
  "region": "eu-west-1",
  "resources": [
    "arn:aws:geo:eu-west-1:0123456789101:tracker/Tracker_EXAMPLE"
  ],
  "detail": {
    "EventType": "UPDATE",
    "TrackerName": "tracker_2",
    "DeviceId": "Device1-EXAMPLE",
    "SampleTime": "2020-11-10T23:41:43.826Z",
    "ReceivedTime": "2020-11-10T23:41:39.235Z",
    "Position": [
      -123.08569321875426,
      49.23766166742559
    ],
    "Accuracy": {
      "Horizontal": 15.3
    },
    "PositionProperties": {
      "ExampleKey1": "ExampleField1",
      "ExampleKey2": "ExampleField2"
    }
  }
}
```
