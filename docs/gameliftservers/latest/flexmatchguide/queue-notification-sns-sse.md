# Set up an SNS topic with server-side encryption

You can use server-side encryption (SSE) to store sensitive data in encrypted topics. SSE
protects the contents of messages in Amazon SNS topics using keys managed in AWS Key Management Service (AWS KMS). For
more information about server-side encryption with Amazon SNS, see [Encryption at rest](../../../sns/latest/dg/sns-server-side-encryption.md "../../../sns/latest/dg/sns-server-side-encryption.md") in the
_Amazon Simple Notification Service Developer Guide_.

To set up an SNS topic with server-side encryption, review the following topics:

- [Creating key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_
- [Enabling SSE for a topic](../../../sns/latest/dg/sns-enable-encryption-for-topic.md "../../../sns/latest/dg/sns-enable-encryption-for-topic.md") in the _Amazon Simple Notification Service Developer Guide_
  When creating your KMS key, use the following KMS key policy:

```
{
  "Effect": "Allow",
  "Principal": {
    "Service": "gamelift.amazonaws.com"
  },
  "Action": [
      "kms:Decrypt",
      "kms:GenerateDataKey"
  ],
  "Resource": "*",
  "Condition": {
      "ArnLike": {
        "aws:SourceArn": "arn:aws:gamelift:`your_region`:`your_account`:matchmakingconfiguration/`your_configuration_name`"
      },
      "StringEquals": {
        "kms:EncryptionContext:aws:sns:topicArn": "arn:aws:sns:`your_region`:`your_account`:`your_sns_topic_name`"
      }
  }
}
```
