# Securing Amazon SNS data with server-side

encryption

Server-side encryption (SSE) lets you store sensitive data in encrypted topics by protecting
the contents of messages in Amazon SNS topics using keys managed in AWS Key Management Service (AWS KMS).

SSE encrypts messages as soon as Amazon SNS receives them. The messages are stored in encrypted
form, and only decrypted when they are sent.

- For information about managing SSE using the AWS Management Console or the AWS SDK for Java (by setting the
  `KmsMasterKeyId` attribute using the `CreateTopic` and `SetTopicAttributes` API
  actions), see [Setting up Amazon SNS topic encryption with
  server-side encryption](sns-enable-encryption-for-topic.md "sns-enable-encryption-for-topic.md").
- For information about creating encrypted topics using AWS CloudFormation (by setting the
  `KmsMasterKeyId` property using the `AWS::SNS::Topic`
  resource), see the _AWS CloudFormation User Guide_.

###### Important

All requests to topics with SSE enabled must use HTTPS and [Signature Version 4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").

For information about compatibility of other services with encrypted topics, see your
service documentation.

Amazon SNS only supports symmetric encryption KMS keys. You cannot use any other type of
KMS key to encrypt your service resources. For help determining whether a KMS key is a
symmetric encryption key, see [Identifying asymmetric
KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md").

AWS KMS combines secure, highly available hardware and software to provide a key management
system scaled for the cloud. When you use Amazon SNS with AWS KMS, the [data keys](#sse-key-terms "#sse-key-terms") that encrypt your message data are also encrypted and stored with the data
they protect.

The following are benefits of using AWS KMS:

- You can create and manage the [AWS KMS key](#sse-key-terms "#sse-key-terms")
  yourself.
- You can also use AWS-managed KMS keys for Amazon SNS, which are unique for each account
  and region.
- The AWS KMS security standards can help you meet encryption-related compliance
  requirements.
  For more information, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
  in the _AWS Key Management Service Developer Guide_.

## Encryption scope

SSE encrypts the body of a message in an Amazon SNS topic.

SSE doesn't encrypt the following:

- Topic metadata (topic name and attributes)
- Message metadata (subject, message ID, timestamp, and attributes)
- Data protection policy
- Per-topic metrics

###### Note

- A message is encrypted only if it is sent after the encryption of a topic is
  enabled. Amazon SNS doesn't encrypt backlogged messages.
- Any encrypted message remains encrypted even if the encryption of its topic is
  disabled.

## Key terms

The following key terms can help you better understand the functionality of SSE. For
detailed descriptions, see the _[Amazon Simple Notification Service API Reference](../api.md "../api.md")_.

**Data key**

The data encryption key (DEK) responsible for encrypting the contents of Amazon SNS
messages.

For more information, see [Data
Keys](../../../kms/latest/developerguide/concepts.md#data-keys "../../../kms/latest/developerguide/concepts.md#data-keys") in the _AWS Key Management Service Developer Guide_ and [Envelope
Encryption](../../../encryption-sdk/latest/developer-guide/how-it-works.md#envelope-encryption "../../../encryption-sdk/latest/developer-guide/how-it-works.md#envelope-encryption") in the _AWS Encryption SDK Developer Guide_.

**AWS KMS key ID**

The alias, alias ARN, key ID, or key ARN of an AWS KMS key, or a custom
AWS KMS—in your account or in another account. While the alias of the AWS managed
AWS KMS for Amazon SNS is always `alias/aws/sns`, the alias of a custom AWS KMS can,
for example, be `alias/`MyAlias``. You can use these
AWS KMS keys to protect the messages in Amazon SNS topics.

###### Note

Keep the following in mind:

- The first time you use the AWS Management Console to specify the AWS managed KMS for Amazon SNS for a
  topic, AWS KMS creates the AWS managed KMS for Amazon SNS.
- Alternatively, the first time you use the `Publish` action on a topic with
  SSE enabled, AWS KMS creates the AWS managed KMS for Amazon SNS.

You can create AWS KMS keys, define the policies that control how AWS KMS keys can be
used, and audit AWS KMS usage using the **AWS KMS keys** section of
the AWS KMS console or the `CreateKey` AWS KMS action. For more information, see [AWS KMS keys](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys") and [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
_AWS Key Management Service Developer Guide_. For more examples of AWS KMS identifiers, see
[KeyId](../../../kms/latest/APIReference/API_DescribeKey.md#API_DescribeKey_RequestParameters "../../../kms/latest/APIReference/API_DescribeKey.md#API_DescribeKey_RequestParameters") in the _AWS Key Management Service API Reference_. For information about
finding AWS KMS identifiers, see [Find the Key ID and ARN](../../../kms/latest/developerguide/viewing-keys.md#find-cmk-id-arn "../../../kms/latest/developerguide/viewing-keys.md#find-cmk-id-arn")
in the _AWS Key Management Service Developer Guide_.

###### Important

There are additional charges for using AWS KMS. For more information, see [Estimating AWS KMS costs](sns-key-management.md#sse-estimate-kms-usage-costs "sns-key-management.md#sse-estimate-kms-usage-costs") and [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing "https://aws.amazon.com/kms/pricing").
