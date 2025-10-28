# CloudWatch Logs

The CloudWatch Logs (`cloudwatchLogs`) action sends data to Amazon CloudWatch Logs. You can
use `batchMode` to upload and timestamp multiple device log records in
one message. You can also specify the log group where the action sends data.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `logs:CreateLogStream`,
  `logs:DescribeLogStreams`, and
  `logs:PutLogEvents` operations. For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

- If you use a customer managed AWS KMS key (KMS key) to encrypt
  log data in CloudWatch Logs, the service must have permission to use the KMS key
  on the caller's behalf. For more information, see [Encrypt log data in
  CloudWatch Logs using AWS KMS](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the _Amazon CloudWatch Logs User
  Guide_.

## MQTT message format

requirements for `batchMode`

If you use the CloudWatch Logs rule action with `batchMode` turned off, there
are no MQTT message formatting requirements. (Note: the `batchMode`
parameter's default value is `false`.) However, if you use the CloudWatch Logs
rule action with `batchMode` turned on (the parameter value is
`true`), MQTT messages containing device-side logs must be
formatted to contain a timestamp and a message payload. **Note:**
`timestamp` represents the time that the event occurred and is
expressed as a number of milliseconds after January 1, 1970 00:00:00 UTC.

The following is an example of the publish format:

```
[
  {"timestamp": 1673520691093, "message": "Test message 1"},
  {"timestamp": 1673520692879, "message": "Test message 2"},
  {"timestamp": 1673520693442, "message": "Test message 3"}
]
```

Depending on how the device-side logs are generated, they might need to be
filtered and reformatted before they're sent to comply with this requirement.
For more information, see [MQTT Message
payload](topicdata.md "topicdata.md").

Independent of the `batchMode` parameter, `message`
contents must comply with AWS IoT message size limitations. For more information,
see [AWS IoT Core
endpoints and quotas](../../../general/latest/gr/iot-core.md "../../../general/latest/gr/iot-core.md").

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`logGroupName`

The CloudWatch log group where the action sends data.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

`roleArn`

The IAM role that allows access to the CloudWatch log group. For more
information, see [Requirements](#cloudwatch-logs-rule-action-requirements "#cloudwatch-logs-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

(optional) `batchMode`

Indicates whether batches of log records will be extracted and
uploaded into CloudWatch. Values include `true` or
`false` (default). For more information, see [Requirements](#cloudwatch-logs-rule-action-requirements "#cloudwatch-logs-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines a CloudWatch Logs action in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "cloudwatchLogs": {
                    "logGroupName": "IotLogs",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_cw",
                    "batchMode": false
                }
            }
        ]
    }
}
```

## See also

- [What is Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md") in the
  _Amazon CloudWatch Logs User Guide_
