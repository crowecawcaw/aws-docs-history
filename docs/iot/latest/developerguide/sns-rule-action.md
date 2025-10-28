# SNS

The SNS (`sns`) action sends the data from an MQTT message as an
Amazon Simple Notification Service (Amazon SNS) push notification.

You can follow a tutorial that shows you how to create and test a rule with an SNS
action. For more information, see [Tutorial: Sending an Amazon SNS notification](iot-sns-rule.md "iot-sns-rule.md").

###### Note

The SNS action doesn't support [Amazon SNS FIFO (First-In-First-Out)
topics](../../../sns/latest/dg/sns-fifo-topics.md "../../../sns/latest/dg/sns-fifo-topics.md"). Because the rules engine is a fully distributed service,
there is no guarantee of message order when the SNS action is invoked.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `sns:Publish` operation. For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

- If you use an AWS KMS customer managed-managed AWS KMS key to encrypt
  data at rest in Amazon SNS, the service must have permission to use the
  AWS KMS key on the caller's behalf. For more information, see [Key management](../../../sns/latest/dg/sns-key-management.md "../../../sns/latest/dg/sns-key-management.md") in
  the _Amazon Simple Notification Service Developer Guide_.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`targetArn`

The SNS topic or individual device to which the push notification
is sent.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

`messageFormat`

(Optional) The message format. Amazon SNS uses this setting to
determine if the payload should be parsed and if relevant
platform-specific parts of the payload should be extracted. Valid
values: `JSON`, `RAW`. Defaults to
`RAW`.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`roleArn`

The IAM role that allows access to SNS. For more information,
see [Requirements](#sns-rule-action-requirements "#sns-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines an SNS action in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "sns": {
                    "targetArn": "arn:aws:sns:us-east-2:123456789012:my_sns_topic",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_sns"
                }
            }
        ]
    }
}
```

The following JSON example defines an SNS action with substitution templates
in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "sns": {
                    "targetArn": "arn:aws:sns:us-east-1:123456789012:${topic()}",
                    "messageFormat": "JSON",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_sns"
                }
            }
        ]
    }
}
```

## See also

- [What is Amazon Simple Notification Service?](../../../sns/latest/dg.md "../../../sns/latest/dg.md") in the
  _Amazon Simple Notification Service Developer Guide_
- [Tutorial: Sending an Amazon SNS notification](iot-sns-rule.md "iot-sns-rule.md")
