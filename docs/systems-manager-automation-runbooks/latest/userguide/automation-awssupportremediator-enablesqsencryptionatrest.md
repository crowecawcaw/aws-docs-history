

# `AWSSupportRemediator-EnableSqsEncryptionAtRest`

**Description**

Enables server-side encryption (SSE) for an Amazon Simple Queue Service (Amazon SQS) queue.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [Amazon SQS queues should be encrypted at rest](https://docs.aws.amazon.com/securityhub/latest/userguide/sqs-controls.html#sqs-1).

If the queue does not exist, or if the queue already has server-side encryption enabled, the automation completes successfully without making changes.

You must choose exactly one type of server-side encryption. Set `SqsManagedSseEnabled` to `true` to use Amazon SQS managed encryption keys (SSE-SQS). To use an AWS Key Management Service (AWS KMS) key (SSE-KMS) instead, provide `KMSKeyId`. Providing both at the same time causes the automation to fail. If neither is provided, the automation defaults to SSE-KMS using the AWS managed key `alias/aws/sqs`.

When you use SSE-KMS, message producers and consumers that interact with the queue must have `kms:GenerateDataKey` and `kms:Decrypt` permissions on the specified AWS KMS key. Queues that rely on roles or users without these permissions might stop sending or receiving messages after you enable SSE-KMS.

To roll back the change, call Amazon SQS `SetQueueAttributes` with the initial values from `validateQueue.InitialSqsManagedSseEnabled`, `validateQueue.InitialKmsMasterKeyId`, and `validateQueue.InitialKmsDataKeyReusePeriodSeconds`.

Using SSE-KMS might incur additional AWS KMS request charges. For more information about pricing, see [Amazon SQS pricing](https://aws.amazon.com/sqs/pricing/) and [AWS KMS pricing](https://aws.amazon.com/kms/pricing/).

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ QueueName

  Type: String

  Description: (Required) The name of the Amazon SQS queue for which to enable server-side encryption.
+ KMSKeyId

  Type: String

  Description: (Conditional) The AWS KMS key ID, multi-region key ID, or key alias to use for server-side encryption. Only applicable when `SqsManagedSseEnabled` is `false`. When empty, the automation uses `alias/aws/sqs`.
+ KmsDataKeyReusePeriodSeconds

  Type: Integer

  Description: (Optional) The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. Must be between 60 seconds and 86400 seconds (24 hours). Has no effect when `SqsManagedSseEnabled` is `true`.

  Default: 300
+ SqsManagedSseEnabled

  Type: Boolean

  Description: (Optional) Whether to enable server-side encryption using Amazon SQS managed encryption keys. Set to `false` to use an AWS KMS key instead.

  Default: False

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `sqs:GetQueueAttributes`
+ `sqs:GetQueueUrl`
+ `sqs:SetQueueAttributes`

**Document Steps**

1. **validateQueue** - Validates the requested encryption inputs, confirms that the Amazon SQS queue exists, and determines whether to enable server-side encryption.

1. **branchOnChangeRequired** - Branches on whether to enable server-side encryption on the queue.

1. **enableSqsEncryption** - Enables server-side encryption for the Amazon SQS queue by setting the required queue attributes.

**Outputs**
+ validateQueue.ChangeRequired: Whether to enable server-side encryption on the queue.
+ validateQueue.ValidationMessage: Information about the validation result.
+ validateQueue.InitialSqsManagedSseEnabled: The initial value of `SqsManagedSseEnabled` on the queue before the change. Empty string when the queue does not exist.
+ validateQueue.InitialKmsMasterKeyId: The initial value of `KmsMasterKeyId` on the queue before the change. Empty string when the queue does not exist or SSE-KMS was not previously configured.
+ validateQueue.InitialKmsDataKeyReusePeriodSeconds: The initial value of `KmsDataKeyReusePeriodSeconds` on the queue before the change. Empty string when the queue does not exist or SSE-KMS was not previously configured.