# AWS IoT Events

The AWS IoT Events (`iotEvents`) action sends data from an MQTT message to an
AWS IoT Events input.

###### Important

If the payload is sent to AWS IoT Core without the `Input attribute
 Key`, or if the key isn't in the same JSON path specified in the key,
it will cause the IoT rule to fail with the error `Failed to send message
 to Iot Events`.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `iotevents:BatchPutMessage` operation.
  For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`batchMode`

(Optional) Whether to process the event actions as a batch. The
default value is `false`.

When `batchMode` is `true` and the rule SQL
statement evaluates to an Array, each Array element is treated as a
separate message when it's sent to AWS IoT Events by calling [`BatchPutMessage`](../../../iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.md "../../../iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.md"). The resulting array
can't have more than 10 messages.

When `batchMode` is `true`, you can't
specify a `messageId`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`inputName`

The name of the AWS IoT Events input.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

`messageId`

(Optional) Use this to verify that only one input (message) with a
given `messageId` is processed by an AWS IoT Events detector. You
can use the `${newuuid()}` substitution template to
generate a unique ID for each request.

When `batchMode` is `true`, you can't
specify a `messageId`--a new UUID value will be
assigned.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`roleArn`

The IAM role that allows AWS IoT to send an input to an AWS IoT Events
detector. For more information, see [Requirements](#iotevents-rule-action-requirements "#iotevents-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines an IoT Events action in an AWS IoT
rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "iotEvents": {
                    "inputName": "MyIoTEventsInput",
                    "messageId": "${newuuid()}",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_events"
                }
            }
        ]
    }
}
```

## See also

- [What is AWS IoT Events?](../../../iotevents/latest/developerguide.md "../../../iotevents/latest/developerguide.md") in the
  _AWS IoT Events Developer Guide_
