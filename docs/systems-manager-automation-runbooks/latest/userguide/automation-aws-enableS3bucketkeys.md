# `AWS-EnableS3BucketKeys`

**Description**

The `AWS-EnableS3BucketKeys` runbook enables Bucket Keys on the
Amazon Simple Storage Service (Amazon S3) bucket you specify. This bucket level key creates data keys for new
objects during its lifecycle. If you don't specify a value for the
`KmsKeyId` parameter, server-side encryption using Amazon S3 managed keys
(SSE-S3) are used for the default encryption configuration.

###### Note

Amazon S3 Bucket Keys aren't supported for dual-layer server-side encryption with
AWS Key Management Service (AWS KMS) keys (DSSE-KMS).

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableS3BucketKeys "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableS3BucketKeys")

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

- BucketName

Type: String

Description: (Required) The name of the S3 bucket you want to enable
Bucket Keys for.

- KMSKeyId

Type: String

Description: (Optional) The Amazon Resource Name (ARN), key ID, or the
key alias of the AWS Key Management Service (AWS KMS) customer managed key you want to use for
server-side encryption.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `s3:GetEncryptionConfiguration`
- `s3:PutEncryptionConfiguration`

**Document Steps**

- ChooseEncryptionType (aws:branch) - Evaluates the value provided for the
  `KmsKeyId` parameter to determine if SSE-S3 (AES256) or
  SSE-KMS will be used.
- PutBucketKeysKMS (aws:executeAwsApi) - Sets the
  `BucketKeyEnabled` property to `true` for the
  specified S3 bucket using the specified `KmsKeyId`.
- PutBucketKeysAES256 (aws:executeAwsApi) - Sets the
  `BucketKeyEnabled` property to `true` for the
  specified S3 bucket with AES256 encryption.
- VerifyS3BucketKeysEnabled (aws:assertAwsResourceProperty) - Verifies that
  the Bucket Keys are enabled on the target S3 bucket.
