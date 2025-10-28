# `AWS-ArchiveS3BucketToIntelligentTiering`

**Description**

The `AWS-ArchiveS3BucketToIntelligentTiering` runbook creates, or
replaces, an intelligent tiering configuration for the Amazon Simple Storage Service (Amazon S3) bucket you
specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ArchiveS3BucketToIntelligentTiering "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ArchiveS3BucketToIntelligentTiering")

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

Description: (Required) The name of the S3 bucket you want to create an
intelligent tiering configuration for.

- ConfigurationId

Type: String

Description: (Required) The ID for the intelligent tiering configuration.
This can be a new configuration ID, or the ID of an existing
configuration.

- NumberOfDaysToArchive

Type: String

Valid values: 90-730

Description: (Required) The number of consecutive days after an object in
your bucket is eligible to be transitioned to the Archive Access
tier.

- NumberOfDaysToDeepArchive

Type: String

Valid values: 180-730

Description: (Required) The number of consecutive days after an object in
your bucket is eligible to be transitioned to the Deep Archive Access
tier.

- S3Prefix

Type: String

Description: (Optional) The key name prefix of the objects you want to
apply the configuration to.

- Tags

Type: MapList

Description: (Optional) Metadata assigned to the objects you want to apply
the configuration to. Tags consist of a user-defined key and value.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `s3:GetIntelligentTieringConfiguration`
- `s3:PutIntelligentTieringConfiguration`

**Document Steps**

- PutsBucketIntelligentTieringConfiguration (aws:executeScript) - Creates or
  updates an Amazon S3 Intelligent-Tiering configuration for the specified
  bucket.
- VerifyBucketIntelligentTieringConfiguration
  (aws:assertAwsResourceProperty) - Verifies the S3 Bucket Intelligent
  Configuration was applied to the specified bucket.
