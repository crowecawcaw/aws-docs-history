End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Create a detector model to represent device

states in AWS IoT Events

In [Create an AWS IoT Events input to capture device data](iotevents-create-input.md "iotevents-create-input.md"), you
created an `input` based on a message that reports pressure data from a motor. To
continue with the example, here is a detector model that responds to an over-pressure event
in a motor.

You create two states: "`Normal`", and "`Dangerous`". Each
detector (instance) enters the "`Normal`" state when it's created. The instance
is created when an input with a unique value for the `key` "`motorid`"
arrives.

If the detector instance receives a pressure reading of 70 or greater, it enters the
"`Dangerous`" state and sends an Amazon SNS message as a warning. If the pressure
readings return to normal (less than 70) for three consecutive inputs, the detector returns
to the "`Normal`" state and sends another Amazon SNS message as an all clear.

This example detector model assumes you have created two Amazon SNS topics whose Amazon
Resource Names (ARNs) are shown in the definition as `"targetArn":
 "arn:aws:sns:us-east-1:123456789012:underPressureAction"` and
`"targetArn":
 "arn:aws:sns:us-east-1:123456789012:pressureClearedAction"`.

For more information, see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md") and, more specifically, the documentation of
the [CreateTopic](../../../sns/latest/api/API_CreateTopic.md "../../../sns/latest/api/API_CreateTopic.md") operation in the
_Amazon Simple Notification Service API Reference_.

This example also assumes you have created an AWS Identity and Access Management (IAM) role with appropriate
permissions. The ARN of this role is shown in the detector model definition as
`"roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole"`. Follow the
steps in [Setting up permissions for AWS IoT Events](iotevents-permissions.md "iotevents-permissions.md") to
create this role and copy the ARN of the role in the appropriate place in the detector model
definition.

You can create the detector model using the following AWS CLI command.

```

aws iotevents create-detector-model  --cli-input-json file://motorDetectorModel.json
```

The file `"motorDetectorModel.json"` contains the following.

```
{
  "detectorModelName": "motorDetectorModel",
  "detectorModelDefinition": {
    "states": [
      {
        "stateName": "Normal",
        "onEnter": {
          "events": [
            {
              "eventName": "init",
              "condition": "true",
              "actions": [
                {
                  "setVariable": {
                    "variableName": "pressureThresholdBreached",
                    "value": "0"
                  }
                }
              ]
            }
          ]
        },
        "onInput": {
          "transitionEvents": [
            {
              "eventName": "Overpressurized",
              "condition": "$input.PressureInput.sensorData.pressure > 70",
              "actions": [
                {
                  "setVariable": {
                    "variableName": "pressureThresholdBreached",
                    "value": "$variable.pressureThresholdBreached + 3"
                  }
                }
              ],
              "nextState": "Dangerous"
            }
          ]
        }
      },
      {
        "stateName": "Dangerous",
        "onEnter": {
          "events": [
            {
              "eventName": "Pressure Threshold Breached",
              "condition": "$variable.pressureThresholdBreached > 1",
              "actions": [
                {
                  "sns": {
                    "targetArn": "arn:aws:sns:us-east-1:123456789012:underPressureAction"
                  }
                }
              ]
            }
          ]
        },
        "onInput": {
          "events": [
            {
              "eventName": "Overpressurized",
              "condition": "$input.PressureInput.sensorData.pressure > 70",
              "actions": [
                {
                  "setVariable": {
                    "variableName": "pressureThresholdBreached",
                    "value": "3"
                  }
                }
              ]
            },
            {
              "eventName": "Pressure Okay",
              "condition": "$input.PressureInput.sensorData.pressure <= 70",
              "actions": [
                {
                  "setVariable": {
                    "variableName": "pressureThresholdBreached",
                    "value": "$variable.pressureThresholdBreached - 1"
                  }
                }
              ]
            }
          ],
          "transitionEvents": [
            {
              "eventName": "BackToNormal",
              "condition": "$input.PressureInput.sensorData.pressure <= 70 && $variable.pressureThresholdBreached <= 1",
              "nextState": "Normal"
            }
          ]
        },
        "onExit": {
          "events": [
            {
              "eventName": "Normal Pressure Restored",
              "condition": "true",
              "actions": [
                {
                  "sns": {
                    "targetArn": "arn:aws:sns:us-east-1:123456789012:pressureClearedAction"
                  }
                }
              ]
            }
          ]
        }
      }
    ],
    "initialStateName": "Normal"
  },
  "key" : "motorid",
  "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole"
}
```
