

# Geofencing with Amazon Location Service and AWS IoT
<a name="geofencing-amazon-location-service-iot"></a>

Publication date: **December 21, 2020 ([Diagram history](#geofence-history))**

With this architecture, you can track high-value equipment leaving or entering premises and generate alert notifications. The solution integrates [Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/) with [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) to send asset coordinates to Location Service Trackers. The trackers generate and act on geofence enter and exit events through [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/).

This scenario uses Bluetooth Low Energy (BLE) tagged asset locations in a warehouse with an arbitrary x, y coordinate system. You can also use GPS coordinates outdoors.

## Geofencing with Amazon Location Service diagram
<a name="geofence-diagram"></a>

![Reference architecture diagram showing how to track assets and generate geofence alerts by using Amazon Location Service, AWS IoT Core, Lambda, and EventBridge.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/geofencing-amazon-location-service-iot/images/geofencing-amazon-location-service-iot.png)


The following steps describe the architecture:

1. Create a Geofence Collection resource in Amazon Location Service and add one or more geofences. Create a Location Tracker resource and associate it with the geofence collection. This configures the service to send geofence events to EventBridge.

1. Publish asset position to AWS IoT Core directly or through [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/). With AWS IoT Core in the path, you can manage asset metadata through IoT Thing models.

1. Configure an IoT rule in AWS IoT Core to invoke a [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function.

1. Write a Lambda function to send the location (DeviceID, x, y) to the Location Tracker.

1. The Location Tracker maintains device position history, and the associated geofence collection publishes enter and exit events to the default event bus in EventBridge.

1. Configure EventBridge to invoke a Lambda function for the event received from the service.

1. (Optional) Configure an EventBridge rule to invoke a Lambda function for further processing of raw geofence events.

1. (Optional) Add a Lambda function to forward events to AWS IoT Events for complex event detection. Store event history as a time series in Amazon Timestream.

1. Publish the event to an [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) topic directly from EventBridge to notify the end user.

1. Publish complex events detected by AWS IoT Events to an Amazon SNS topic to notify the end user.

## Further reading
<a name="geofence-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="geofence-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#geofence-history) | Reference architecture diagram first published. | December 21, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.