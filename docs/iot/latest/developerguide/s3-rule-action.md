# S3

The S3 (`s3`) action writes the data from an MQTT message to an
Amazon Simple Storage Service (Amazon S3) bucket.

## Requirements

This rule action has the following requirements:

- An IAM role that AWS IoT can assume to perform the `s3:PutObject` operation.
  For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").

In the AWS IoT console, you can choose or create a role to allow AWS IoT to perform this rule action.

- If you use an AWS KMS customermanaged AWS KMS key to encrypt data at
  rest in Amazon S3, the service must have permission to use the AWS KMS key
  on the caller's behalf. For more information, see [AWS managed AWS KMS keys and customer managed
  AWS KMS keys](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md#aws-managed-customer-managed-cmks "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md#aws-managed-customer-managed-cmks") in the _Amazon Simple Storage Service Developer
  Guide_.

## Parameters

When you create an AWS IoT rule with this action, you must specify the following information:

`bucket`

The Amazon S3 bucket to which to write data.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): API and AWS CLI only

`cannedacl`

(Optional) The Amazon S3 canned ACL that controls access to the object
identified by the object key. For more information, including
allowed values, see [Canned
ACL](../../../AmazonS3/latest/userguide/acl-overview.md#canned-acl "../../../AmazonS3/latest/userguide/acl-overview.md#canned-acl").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`key`

The path to the file where the data is written.

Consider an example where this parameter is
`${topic()}/${timestamp()}` and the rule receives a
message where the topic is `some/topic`. If the current
timestamp is `1460685389`, then this action writes the
data to a file called `1460685389` in the
`some/topic` folder of the S3 bucket.

###### Note

If you use a static key, AWS IoT overwrites a single file each
time the rule invokes. We recommend that you use the message
timestamp or another unique message identifier so that a new
file is saved in Amazon S3 for each message received.

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes

`roleArn`

The IAM role that allows access to the Amazon S3 bucket. For more
information, see [Requirements](#s3-rule-action-requirements "#s3-rule-action-requirements").

Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

## Examples

The following JSON example defines an S3 action in an AWS IoT rule.

```
{
    "topicRulePayload": {
        "sql": "SELECT * FROM 'some/topic'",
        "ruleDisabled": false,
        "awsIotSqlVersion": "2016-03-23",
        "actions": [
            {
                "s3": {
                    "bucketName": "amzn-s3-demo-bucket",
                    "cannedacl": "public-read",
                    "key": "${topic()}/${timestamp()}",
                    "roleArn": "arn:aws:iam::123456789012:role/aws_iot_s3"
                }
            }
        ]
    }
}

```

## See also

- [What is Amazon S3?](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md") in the
  _Amazon Simple Storage Service User Guide_
