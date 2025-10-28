# Topic policies for Amazon SNS topics

The Amazon SNS topic requires the appropriate topic policy to grant access to AWS End User Messaging SMS if they are
not provided in the `TwoChannelWayRole` parameter.

```
{
  "Effect": "Allow",
  "Principal": {
    "Service": "sms-voice.amazonaws.com"
  },
  "Action": "sns:Publish",
  "Resource": "`snsTopicArn`"
}
```

In the preceding example, make the following changes:

- Replace `snsTopicArn` with the Amazon SNS topic that will send
  and receive messages.

###### Note

Amazon SNS FIFO topics are not supported.

Although AWS End User Messaging SMS data is encrypted, you can use Amazon SNS topics that are encrypted using AWS KMS
keys for an additional level of security. This added security can be helpful if your
application handles private or sensitive data.

You need to perform some additional setup steps to use encrypted Amazon SNS topics with two-way
messaging.

The following example statement uses the, optional but recommended,
`SourceAccount` and `SourceArn` conditions to avoid the confused
deputy problem and only the AWS End User Messaging SMS owner account has access. For more information on the
confused deputy problem, see [The confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in the _[IAM user
guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md")_.

First, the key that you use must be _symmetric_. Encrypted Amazon SNS topics
don't support asymmetric AWS KMS keys.

Second, the key policy must be modified to allow AWS End User Messaging SMS to use the key. Add the following
permissions to the existing key policy:

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "sms-voice.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey*",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`accountId`"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:sms-voice:`region`:`accountId`:*"
        }
     }
}
```

For more information about editing key policies, see [Changing a key policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md") in the
_AWS Key Management Service Developer Guide_.

For more information about encrypting Amazon SNS topics using AWS KMS keys, see [Enable
compatibility between event sources from AWS services and encrypted topics](../../../sns/latest/dg/sns-key-management.md#compatibility-with-aws-services "../../../sns/latest/dg/sns-key-management.md#compatibility-with-aws-services") in
the _Amazon Simple Notification Service Developer Guide_.
