# Kinesis Data Streams

The Kinesis Data Streams (`kinesis`) action writes data from an MQTT message to
Amazon Kinesis Data Streams.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `kinesis:PutRecord` operation.
  For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

- If you use an AWS KMS customer-managed AWS KMS key (KMS key) to
  encrypt data at rest in Kinesis Data Streams, the service must have permission to use
  the AWS KMS key on the caller's behalf. For more information, see
  [Permissions
  to use user-generated AWS KMS keys](../../../streams/latest/dev/permissions-user-key-KMS.md "../../../streams/latest/dev/permissions-user-key-KMS.md") in the
  _Amazon Kinesis Data Streams Developer Guide_.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`stream`

The Kinesis data stream to which to write data.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

`partitionKey`

The partition key used to determine to which shard the data is
written. The partition key is usually composed of an expression (for
example, `${topic()}` or
`${timestamp()}`).

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`roleArn`

The ARN of the IAM role that grants AWS IoT permission to access
the Kinesis data stream. For more information, see [Requirements](#kinesis-rule-action-requirements "#kinesis-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines a Kinesis Data Streams action in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "kinesis": {
                    "streamName": "my_kinesis_stream",
                    "partitionKey": "${topic()}",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_kinesis"
                }
            }
        ]
    }
}
```

The following JSON example defines a Kinesis action with substitution templates
in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "kinesis": {
                    "streamName": "${topic()}",
                    "partitionKey": "${timestamp()}",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_kinesis"
                }
            }
        ]
    }
}
```

## See also

- [What is Amazon Kinesis Data Streams?](../../../streams/latest/dev.md "../../../streams/latest/dev.md") in the
  _Amazon Kinesis Data Streams Developer Guide_
