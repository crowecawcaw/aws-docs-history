# Firehose

The Firehose(`firehose`) action sends data from an MQTT message to an
Amazon Data Firehose stream.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `firehose:PutRecord` operation.
  For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

- If
  you use Firehose to send data to an Amazon S3 bucket, and you use an AWS KMS
  customer managed AWS KMS key to encrypt data at rest in Amazon S3, Firehose
  must have access to your bucket and permission to use the AWS KMS key
  on the caller's behalf. For more information, see
  [Grant
  Firehose access to an Amazon S3 destination](../../../firehose/latest/dev/controlling-access.md#using-iam-s3 "../../../firehose/latest/dev/controlling-access.md#using-iam-s3") in the
  _Amazon Data Firehose Developer Guide_.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`batchMode`

(Optional) Whether to deliver the Firehose stream as a batch by using
[`PutRecordBatch`](../../../firehose/latest/APIReference/API_PutRecordBatch.md "../../../firehose/latest/APIReference/API_PutRecordBatch.md") . The default value is
`false`.

When `batchMode` is `true` and the rule's
SQL statement evaluates to an Array, each Array element forms one
record in the `PutRecordBatch` request. The resulting
array can't have more than 500 records.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`deliveryStreamName`

The Firehose stream to which to write the message data.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

`separator`

(Optional) A character separator that is used to separate records
written to the Firehose stream. If you omit this parameter, the stream
uses no separator. Valid values: `,` (comma),
`\t` (tab), `\n` (newline),
`\r\n` (Windows newline).

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`roleArn`

The IAM role that allows access to the Firehose stream. For more
information, see [Requirements](#kinesis-firehose-rule-action-requirements "#kinesis-firehose-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines a Firehose action in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "firehose": {
                    "deliveryStreamName": "my_firehose_stream",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_firehose"
                }
            }
        ]
    }
}

```

The following JSON example defines a Firehose action with substitution templates
in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "firehose": {
                    "deliveryStreamName": "${topic()}",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_firehose"
                }
            }
        ]
    }
}
```

## See also

- [What is Amazon Data Firehose?](../../../firehose/latest/dev.md "../../../firehose/latest/dev.md") in the
  _Amazon Data Firehose Developer Guide_
