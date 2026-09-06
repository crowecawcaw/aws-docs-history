

# Track using AWS IoT and MQTT with Amazon Location Service
<a name="tracking-using-mqtt"></a>

[MQTT](http://mqtt.org/) is a lightweight and widely adopted messaging protocol designed for constrained devices. AWS IoT Core supports device connections that use the MQTT protocol and MQTT over WebSocket Secure (WSS) protocol. 

[AWS IoT Core](https://aws.amazon.com/iot-core/) connects devices to AWS and enables you to send and receive messages between them. The AWS IoT Core rules engine stores queries about your devices' message topics and enables you to define actions for sending messages to other AWS services, such as Amazon Location Service. Devices that are aware of their location as coordinates can have their locations forwarded to Amazon Location through the rules engine.

**Note**  
Devices may know their own position, for example via built-in GPS. AWS IoT also has support for third party device location tracking. For more information, see [AWS IoT Core Device Location](https://docs.aws.amazon.com/iot/latest/developerguide/device-location.html) in the *AWS IoT Core Developer Guide*.

The following walkthrough describes tracking using AWS IoT Core rules. You can also send the device information to your own AWS Lambda function, if you need to process it before sending to Amazon Location. For more details about using Lambda to process your device locations, see [Use AWS Lambda with MQTT](tracking-using-mqtt-with-lambda.md).

**Topics**
+ [Prerequisite](#mqtt-prerequisite)
+ [Create an AWS IoT Core rule](#mqtt-create-iot-rule)
+ [Test your AWS IoT Core rule in the console](#mqtt-test-iot-rule)
+ [Use AWS Lambda with MQTT](tracking-using-mqtt-with-lambda.md)

## Prerequisite
<a name="mqtt-prerequisite"></a>

Before you can begin tracking, you must complete the following prerequisites:
+ [Create a tracker resource](start-create-tracker.md) that you will send the device location data to.
+ [Create an IAM role](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-role.html) for granting AWS IoT Core access to your tracker.

  When following those steps, use the following policy to give access to your tracker:

  ```
  {
    "Version": "2012-10-17",		 	 	 
    "Statement": [
      {
        "Sid": "WriteDevicePosition",
        "Effect": "Allow",
        "Action": "geo:BatchUpdateDevicePosition",
        "Resource": "arn:aws:geo:*:*:tracker/*"
      }
    ]
  }
  ```

## Create an AWS IoT Core rule
<a name="mqtt-create-iot-rule"></a>

Next, create an AWS IoT Core rule to forward your devices' positional telemetry to Amazon Location Service. For more information about creating rules, see the following topics in the *AWS IoT Core Developer Guide*:
+ [Creating an AWS IoT rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-rule.html) for information about creating a new rule.
+ [Location action](https://docs.aws.amazon.com/iot/latest/developerguide/location-rule-action.html) for information specific to creating a rule for publishing to Amazon Location 

## Test your AWS IoT Core rule in the console
<a name="mqtt-test-iot-rule"></a>

If no devices are currently publishing telemetry that includes location, you can test your rule using the AWS IoT Core console. The console has a test client where you can publish a sample message to verify the results of the solution.

1. Sign in to the AWS IoT Core console at [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/home).

1. In the left navigation, expand **Test**, and choose **MQTT test client**.

1. Under **Publish to a topic**, set the **Topic name** to {{iot/topic}} (or the name of the topic that you set up in your AWS IoT Core rule, if different), and provide the following for the **Message payload**. Replace the timestamp {{1604940328}} with a valid timestamp within the last 30 days (any timestamps older than 30 days are ignored by Amazon Location Service trackers).

   ```
   {
     "payload": {
       "deviceid": "thing123",
       "timestamp": {{1604940328}},
       "location": { "lat": 49.2819, "long": -123.1187 },
       "accuracy": { "Horizontal": 20.5 },
       "positionProperties": { "field1": "value1", "field2": "value2" }
     }
   }
   ```

1. Choose **Publish** to topic to send the test message.

1. To validate that the message was received by Amazon Location Service, use the following AWS CLI command. If you modified it during setup, replace the tracker name with the one that you used.

   ```
   aws location batch-get-device-position --tracker-name {{MyTracker}} --device-ids thing123
   ```