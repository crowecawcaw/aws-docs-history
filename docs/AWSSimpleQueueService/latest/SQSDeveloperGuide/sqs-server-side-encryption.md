# Encryption at rest in Amazon SQS

Server-side encryption (SSE) lets you transmit sensitive data in encrypted
queues. SSE protects the contents of messages in queues using SQS-managed
encryption keys (SSE-SQS) or keys managed in the AWS Key Management Service (SSE-KMS). For
information about managing SSE using the AWS Management Console, see the following:

- [Configuring SSE-SQS for a
  queue (console)](sqs-configure-sqs-sse-queue.md "sqs-configure-sqs-sse-queue.md")
- [Configuring SSE-KMS for a
  queue (console)](sqs-configure-sse-existing-queue.md "sqs-configure-sse-existing-queue.md")
  For information about managing SSE using the AWS SDK for Java (and the `CreateQueue`,
  `SetQueueAttributes`, and `GetQueueAttributes` actions), see the following examples:

- [Using server-side encryption with Amazon SQS queues](sqs-java-configure-sse.md "sqs-java-configure-sse.md")
- [Configuring KMS
  permissions for AWS services](sqs-key-management.md#compatibility-with-aws-services "sqs-key-management.md#compatibility-with-aws-services")

SSE encrypts messages as soon as Amazon SQS receives them. The messages are stored in
encrypted form and Amazon SQS decrypts messages only when they are sent to an authorized
consumer.

###### Important

All requests to queues with SSE enabled must use HTTPS and [Signature Version
4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").

An encrypted queue
that uses the default key (AWS managed KMS key for Amazon SQS) cannot invoke a Lambda function in a different AWS account.

Some features of AWS services that can send notifications to Amazon SQS using the
AWS Security Token Service `AssumeRole` action are compatible with SSE but work
_only with standard queues:_

- [Auto Scaling Lifecycle
  Hooks](../../../autoscaling/ec2/userguide/lifecycle-hooks.md "../../../autoscaling/ec2/userguide/lifecycle-hooks.md")
- [AWS Lambda Dead-Letter
  Queues](../../../lambda/latest/dg/dlq.md "../../../lambda/latest/dg/dlq.md")
  For information about compatibility of other services with encrypted queues,
  see [Configure KMS permissions
  for AWS services](sqs-key-management.md#compatibility-with-aws-services "sqs-key-management.md#compatibility-with-aws-services") and your service
  documentation.

AWS KMS combines secure, highly available hardware and software to provide a key
management system scaled for the cloud. When you use Amazon SQS with AWS KMS, the [data keys](#sqs-sse-key-terms "#sqs-sse-key-terms") that encrypt your message data are
also encrypted and stored with the data they protect.

The following are benefits of using AWS KMS:

- You can create and manage [AWS KMS keys](#sqs-sse-key-terms "#sqs-sse-key-terms") yourself.
- You can also use the AWS managed KMS key for Amazon SQS, which is unique
  for each account and region.
- The AWS KMS security standards can help you meet encryption-related
  compliance requirements.
  For more information, see [What is
  AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service Developer Guide_.

## Encryption scope

SSE encrypts the body of a message in an Amazon SQS queue.

SSE doesn't encrypt the following:

- Queue metadata (queue name and attributes)
- Message metadata (message ID, timestamp, and attributes)
- Per-queue metrics

Encrypting a message makes its contents unavailable to unauthorized or
anonymous users. With SSE enabled, anonymous `SendMessage` and
`ReceiveMessage` requests to the encrypted queue will be
rejected. Amazon SQS security best practices recommends against using anonymous
requests. If you wish to send anonymous requests to an Amazon SQS queue, make sure
you disable SSE. This doesn't affect the normal functioning of Amazon SQS:

- A message is encrypted only if it is sent after the encryption of a
  queue is enabled. Amazon SQS doesn't encrypt backlogged messages.
- Any encrypted message remains encrypted even if the encryption of its
  queue is disabled.

Moving a message to a [dead-letter
queue](sqs-dead-letter-queues.md "sqs-dead-letter-queues.md") doesn't affect its encryption:

- When Amazon SQS moves a message from an encrypted source queue to an
  unencrypted dead-letter queue, the message remains encrypted.
- When Amazon SQS moves a message from an unencrypted source queue to an
  encrypted dead-letter queue, the message remains unencrypted.

## Key terms

The following key terms can help you better understand the functionality of
SSE. For detailed descriptions, see the _[Amazon Simple Queue Service API Reference](../APIReference.md "../APIReference.md")_.

**Data key**

The key (DEK) responsible for encrypting the contents of Amazon SQS
messages.

For more information, see [Data Keys](../../../kms/latest/developerguide/concepts.md#data-keys "../../../kms/latest/developerguide/concepts.md#data-keys") in
the _AWS Key Management Service Developer Guide_ in the
_AWS Encryption SDK Developer Guide_.

**Data key reuse period**

The length of time, in seconds, for which Amazon SQS can reuse a data
key to encrypt or decrypt messages before calling AWS KMS again. An
integer representing seconds, between 60 seconds (1 minute) and
86,400 seconds (24 hours). The default is 300 (5 minutes). For more
information, see [Understanding the
data key reuse period](sqs-key-management.md#sqs-how-does-the-data-key-reuse-period-work "sqs-key-management.md#sqs-how-does-the-data-key-reuse-period-work").

###### Note

In the unlikely event of being unable to reach AWS KMS, Amazon SQS
continues to use the cached data key until a connection is
reestablished.

**KMS key ID**

The alias, alias ARN, key ID, or key ARN of an AWS managed
KMS key or a custom KMS key—in your account or in another
account. While the alias of the AWS managed KMS key for Amazon SQS is
always `alias/aws/sqs`, the alias of a custom KMS key
can, for example, be
`alias/`MyAlias``. You can
use these KMS keys to protect the messages in Amazon SQS queues.

###### Note

Keep the following in mind:

- If you don't specify a custom KMS key, Amazon SQS uses
  the AWS managed KMS key for Amazon SQS.
- The first time you use the AWS Management Console to specify the
  AWS managed KMS key for Amazon SQS for a queue, AWS KMS
  creates the AWS managed KMS key for Amazon SQS.
- Alternatively, the first time you use the
  `SendMessage` or
  `SendMessageBatch` action on a queue with
  SSE enabled, AWS KMS creates the AWS managed KMS key
  for Amazon SQS.

You can create KMS keys, define the policies that control how
KMS keys can be used, and audit KMS key usage using the
**Customer managed keys** section of the AWS KMS
console or the `CreateKey` AWS KMS action. For more
information, see [KMS keys](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys") and [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
_AWS Key Management Service Developer Guide_. For more examples of
KMS key identifiers, see [KeyId](../../../kms/latest/APIReference/API_DescribeKey.md#API_DescribeKey_RequestParameters "../../../kms/latest/APIReference/API_DescribeKey.md#API_DescribeKey_RequestParameters") in the _AWS Key Management Service API Reference_. For
information about finding KMS key identifiers, see [Find the
Key ID and ARN](../../../kms/latest/developerguide/viewing-keys.md#find-cmk-id-arn "../../../kms/latest/developerguide/viewing-keys.md#find-cmk-id-arn") in the
_AWS Key Management Service Developer Guide_.

###### Important

There are additional charges for using AWS KMS. For more
information, see [Estimating AWS KMS costs](sqs-key-management.md#sqs-estimate-kms-usage-costs "sqs-key-management.md#sqs-estimate-kms-usage-costs") and [AWS Key Management Service
Pricing](https://aws.amazon.com/kms/pricing "https://aws.amazon.com/kms/pricing").

**Envelope Encryption**

The security of your encrypted data depends in part on protecting
the data key that can decrypt it. Amazon SQS uses the KMS key to
encrypt the data key and then the encrypted data key is stored with
the encrypted message. This practice of using a KMS key to encrypt
data keys is known as envelope encryption.

For more information, see [Envelope Encryption](../../../encryption-sdk/latest/developer-guide/how-it-works.md#envelope-encryption "../../../encryption-sdk/latest/developer-guide/how-it-works.md#envelope-encryption") in the
_AWS Encryption SDK Developer Guide_.
