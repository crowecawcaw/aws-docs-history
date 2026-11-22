

# `AWSSupportRemediator-EnableSnsEncryptionAtRest`

**Description**

Enables server-side encryption (SSE) for an Amazon Simple Notification Service (Amazon SNS) topic using an AWS Key Management Service (AWS KMS) key.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [SNS topics should be encrypted at-rest using AWS KMS](https://docs.aws.amazon.com/securityhub/latest/userguide/sns-controls.html#sns-1).

If the Amazon SNS topic does not exist or server-side encryption (SSE) is already enabled, the automation completes successfully without making changes.

The automation sets the `KmsMasterKeyId` attribute on the Amazon SNS topic to the specified AWS KMS key. To roll back the change, set `KmsMasterKeyId` to the value of `validateTopic.InitialKmsKey` (or to an empty string if `InitialKmsKey` is `N/A`) by calling the `SetTopicAttributes` API.

After enabling server-side encryption (SSE), subscribers and publishers must have `kms:GenerateDataKey` and `kms:Decrypt` permissions on the specified AWS KMS key. If the AWS KMS key policy does not grant these permissions to the subscriber's IAM principal, message delivery can fail.

This requirement applies to cross-account subscribers and AWS service subscribers such as AWS Lambda, Amazon Simple Queue Service (Amazon SQS), and HTTPS endpoints. Review subscriber and AWS KMS key permissions before running this automation. For more information, see [Enabling server-side encryption (SSE) for an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-enable-encryption-for-topic.html).

Using a customer managed AWS KMS key to encrypt an Amazon SNS topic incurs AWS KMS charges for each publish, subscribe, and management call. For more information about pricing, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/).

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
+ TopicArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon SNS topic on which to enable server-side encryption (SSE).
+ KmsKeyId

  Type: String

  Description: (Optional) The AWS KMS key ID, multi-region key ID, or key alias to use for server-side encryption (SSE) on the Amazon SNS topic.

  Default: alias/aws/sns

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `sns:GetTopicAttributes`
+ `sns:SetTopicAttributes`

**Document Steps**

1. **validateTopic** - Validates that the Amazon SNS topic exists and checks whether server-side encryption (SSE) is already enabled.

1. **branchOnChangeRequired** - Branches on whether to enable server-side encryption (SSE) on the Amazon SNS topic.

1. **enableSNSSSE** - Enables server-side encryption (SSE) on the Amazon SNS topic using the specified AWS KMS key.

**Outputs**
+ validateTopic.ChangeRequired: Whether to enable server-side encryption (SSE) on the Amazon SNS topic.
+ validateTopic.InitialKmsKey: The AWS KMS key ID configured on the Amazon SNS topic before execution, or `N/A` if the Amazon SNS topic does not have server-side encryption (SSE) configured.
+ validateTopic.ValidationMessage: A message describing the validation result.