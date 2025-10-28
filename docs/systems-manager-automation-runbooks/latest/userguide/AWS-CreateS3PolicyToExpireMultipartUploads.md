# `AWS-CreateS3PolicyToExpireMultipartUploads`

**Description**

The `AWS-CreateS3PolicyToExpireMultipartUploads` runbook creates a
lifecycle policy for a specified bucket that expires incomplete, multi-part uploads
in progress after a defined number of days. This runbook merges the new lifecycle
policy with any existing lifecycle bucket policies that already exist.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateS3PolicyToExpireMultipartUploads "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateS3PolicyToExpireMultipartUploads")

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

Description: (Required) The name of the S3 bucket you want to
configure.

- DaysUntilExpire

Type: Integer

Description: (Required) The number of days Amazon S3 waits before permanently
removing all parts of the upload.

- RuleId

Type: String

Description: (Required) The ID used to identify the lifeycle bucket rule.
This must be a unique value.

- S3Prefix

Type: String

Description: (Optional) The key name prefix of the objects you want to
apply the configuration to.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetAutomationExecution`
- `ssm:StartAutomationExecution`
- `s3:GetLifecycleConfiguration`
- `s3:PutLifecycleConfiguration`

**Document Steps**

- ConfigureExpireMultipartUploads (aws:executeScript) - Configures the
  lifecycle policy for the bucket.
- VerifyExpireMultipartUploads (aws:executeScript) - Verifies the lifecycle
  policy has been configured for the bucket.

**Outputs**

- `VerifyExpireMultipartUploads.VerifyExpireMultipartUploadsResponse`
- `VerifyExpireMultipartUploads.LifecycleConfigurationRule`
