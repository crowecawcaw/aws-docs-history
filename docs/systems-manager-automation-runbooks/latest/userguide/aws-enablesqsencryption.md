# `AWS-EnableSQSEncryption`

**Description**

The `AWS-EnableSQSEncryption` runbook enables encryption at rest for an Amazon Simple Queue Service (Amazon SQS) queue. An Amazon SQS queue can be encrypted with Amazon SQS managed keys (SSE-SQS), or with AWS Key Management Service (AWS KMS) managed keys (SSE-KMS). The key that you assign to your queue must have a key policy that includes permissions for all principals that are authorized to use the queue. With encryption enabled, anonymous `SendMessage` and `ReceiveMessage` requests to the encrypted queue are rejected.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableSQSEncryption "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableSQSEncryption")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- QueueUrl

Type: String

Description: (Required) The URL of the Amazon SQS queue you want to enable encryption on.

- KmsKeyId

Type: String

Description: (Optional) The AWS KMS key to use for encryption. This value can be a globally unique identifier, an ARN to either an alias or a key, or an alias name prefixed by "alias/". You can also use the AWS managed key by specifying the alias aws/sqs.

- KmsDataKeyReusePeriodSeconds

Type: String

Valid values: 60-86400

Default: 300

Description: (Optional) The length of time, in seconds, an Amazon SQS queue can reuse a data key to encrypt or decrypt messages before calling AWS KMS again.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `sqs:GetQueueAttributes`
- `sqs:SetQueueAttributes`

**Document Steps**

- SelectKeyType (`aws:branch`): Branches based on the key specified.
- PutAttributeSseKms (`aws:executeAwsApi`) - Updates the Amazon SQS queue to use the AWS KMS key specified for encryption.
- PutAttributeSseSqs (`aws:executeAwsApi`) - Updates the Amazon SQS queue to use the default key for encryption.
- VerifySqsEncryptionKms (`aws:assertAwsResourceProperty`) - Verifies encryption is enabled on the Amazon SQS queue.
- VerifySqsEncryptionDefault (`aws:assertAwsResourceProperty`) - Verifies encryption is enabled on the Amazon SQS queue.
