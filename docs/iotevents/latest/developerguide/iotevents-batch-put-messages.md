End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Send messages as inputs to a detector in

AWS IoT Events

You have now defined an input that identifies the important fields in messages sent from
a device (see [Create an AWS IoT Events input to capture device data](iotevents-create-input.md "iotevents-create-input.md")). In the previous section, you created a `detector model` that responds to an
over-pressure event in a motor (see [Create a detector model to represent device
states in AWS IoT Events](iotevents-create-detector.md "iotevents-create-detector.md")).

To complete the example, send messages from a device (in this case a computer with the
AWS CLI installed) as inputs to the detector.

###### Note

When you create a detector model or update an existing one, it takes several minutes
before the new or updated detector model begins to receive messages and create detectors
(instances). If you update the detector model, during this time you might continue to see
behavior based on the previous version.

Use the following AWS CLI command to send a message with data that breaches the
threshold.

```

aws iotevents-data batch-put-message --cli-input-json file://highPressureMessage.json --cli-binary-format raw-in-base64-out
```

The file "`highPressureMessage.json`" contains the following.

```
{
  "messages": [
    {
      "messageId": "00001",
      "inputName": "PressureInput",
      "payload": "{\"motorid\": \"Fulton-A32\", \"sensorData\": {\"pressure\": 80, \"temperature\": 39} }"
    }
  ]
}
```

You must change the `messageId` in each message sent. If you don't change it,
the AWS IoT Events system deduplicates the messages. AWS IoT Events ignores a message if it has the same
`messageID` as another message that was sent within the last five
minutes.

At this point, a detector (instance) is created to monitor events for the motor
`"Fulton-A32"`. This detector enters the `"Normal"` state when it's
created. But because we sent a pressure value above the threshold, it immediately
transitions to the `"Dangerous"` state. As it does so, the detector sends a
message to the Amazon SNS endpoint whose ARN is
`arn:aws:sns:us-east-1:123456789012:underPressureAction`.

Run the following AWS CLI command to send a message with data that is beneath the pressure
threshold.

```

aws iotevents-data batch-put-message --cli-input-json file://normalPressureMessage.json --cli-binary-format raw-in-base64-out
```

The file `normalPressureMessage.json` contains the following.

```
{
  "messages": [
    {
      "messageId": "00002",
      "inputName": "PressureInput",
      "payload": "{\"motorid\": \"Fulton-A32\", \"sensorData\": {\"pressure\": 60, \"temperature\": 29} }"
    }
  ]
}
```

You must change the `messageId` in the file each time you invoke the
`BatchPutMessage` command within a five minute period. Send the message two
more times. After the message is sent three times, the detector (instance) for the motor
"`Fulton-A32`" sends a message to the Amazon SNS endpoint
`"arn:aws:sns:us-east-1:123456789012:pressureClearedAction"` and
reenters the `"Normal"` state.

###### Note

You can send multiple messages at one time with `BatchPutMessage`. However,
the order in which these messages are processed isn't guaranteed. To guarantee messages
(inputs) are processed in order, send them one at a time and wait for a successful
response each time the API is called.

The following are example SNS message payloads created by the detector model example
described in this section.

**on event "Pressure Threshold Breached"**

```
IoT> {
  "eventTime":1558129816420,
  "payload":{
    "actionExecutionId":"5d7444df-a655-3587-a609-dbd7a0f55267",
    "detector":{
      "detectorModelName":"motorDetectorModel",
      "keyValue":"Fulton-A32",
      "detectorModelVersion":"1"
    },
    "eventTriggerDetails":{
      "inputName":"PressureInput",
      "messageId":"00001",
      "triggerType":"Message"
    },
    "state":{
      "stateName":"Dangerous",
      "variables":{
        "pressureThresholdBreached":3
      },
      "timers":{}
    }
  },
  "eventName":"Pressure Threshold Breached"
}
```

**on event "Normal Pressure Restored"**

```
IoT> {
  "eventTime":1558129925568,
  "payload":{
    "actionExecutionId":"7e25fd38-2533-303d-899f-c979792a12cb",
    "detector":{
      "detectorModelName":"motorDetectorModel",
      "keyValue":"Fulton-A32",
      "detectorModelVersion":"1"
    },
    "eventTriggerDetails":{
      "inputName":"PressureInput",
      "messageId":"00004",
      "triggerType":"Message"
    },
    "state":{
      "stateName":"Dangerous",
      "variables":{
        "pressureThresholdBreached":0
      },
      "timers":{}
    }
  },
  "eventName":"Normal Pressure Restored"
}
```

If you have defined any timers, their current state is also shown in the SNS message
payloads.

The message payloads contain information about the state of the detector (instance) at
the time the message was sent (that is, at the time the SNS action was run). You can use the
[https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DescribeDetector.html](../apireference/API_iotevents-data_DescribeDetector.md "../apireference/API_iotevents-data_DescribeDetector.md") operation to get similar information about the state of the detector.
