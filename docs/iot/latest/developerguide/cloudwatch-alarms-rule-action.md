# CloudWatch alarms

The CloudWatch alarm (`cloudWatchAlarm`) action changes the state of an
Amazon CloudWatch alarm. You can specify the state change reason and value in this call.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `cloudwatch:SetAlarmState` operation.
  For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`alarmName`

The CloudWatch alarm name.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

`stateReason`

Reason for the alarm change.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`stateValue`

The value of the alarm state. Valid values: `OK`,
`ALARM`, `INSUFFICIENT_DATA`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`roleArn`

The IAM role that allows access to the CloudWatch alarm. For more
information, see [Requirements](#cloudwatch-alarms-rule-action-requirements "#cloudwatch-alarms-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines a CloudWatch alarm action in an AWS IoT
rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "cloudwatchAlarm": {
                    "alarmName": "IotAlarm",
                    "stateReason": "Temperature stabilized.",
                    "stateValue": "OK",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_cw"
                }
            }
        ]
    }
}
```

## See also

- [What is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md") in the
  _Amazon CloudWatch User Guide_
- [Using Amazon CloudWatch
  alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_
