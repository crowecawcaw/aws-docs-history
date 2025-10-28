# SQS

The SQS (`sqs`) action sends data from an MQTT message to an Amazon Simple Queue Service
(Amazon SQS) queue.

###### Note

The SQS action doesn't support [Amazon SQS
FIFO (First-In-First-Out) queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.md"). Because the rules engine is a
fully distributed service, there is no guarantee of message order when the SQS
action is triggered.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `sqs:SendMessage` operation.
  For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

- If you use an AWS KMS customer managed AWS KMS key to encrypt data at
  rest in Amazon SQS, the service must have permission to use the
  AWS KMS key on the caller's behalf. For more information, see [Key management](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.md") in
  the _Amazon Simple Queue Service Developer Guide_.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`queueUrl`

The URL of the Amazon SQS queue to which to write the data. The region
in this URL doesn't need to be the same AWS Region as your [AWS IoT rule](iot-rules.md "iot-rules.md").

###### Note

There can be additional charges for data transfer cross
AWS Regions using the SQS rule action. For more information,
see [Amazon SQS
pricing](https://aws.amazon.com/sqs/pricing/ "https://aws.amazon.com/sqs/pricing/").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

`useBase64`

Set this parameter to `true` to configure the rule
action to base64-encode the message data before it writes the data
to the Amazon SQS queue. Defaults to `false`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`roleArn`

The IAM role that allows access to the Amazon SQS queue. For more
information, see [Requirements](#sqs-rule-action-requirements "#sqs-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines an SQS action in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "sqs": {
                    "queueUrl": "https://sqs.us-east-2.amazonaws.com/123456789012/my_sqs_queue",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_sqs"
                }
            }
        ]
    }
}

```

The following JSON example defines an SQS action with substitution templates
in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "sqs": {
                    "queueUrl": "https://sqs.us-east-2.amazonaws.com/123456789012/${topic()}",
                    "useBase64": true,
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_sqs"
                }
            }
        ]
    }
}
```

## See also

- [What is Amazon Simple Queue Service?](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide.md") in the
  _Amazon Simple Queue Service Developer Guide_
