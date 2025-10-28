# `AWSConfigRemediation-EnableCloudFrontAccessLogs`

**Description**

The `AWSConfigRemediation-EnableCloudFrontAccessLogs` runbook enables access
logging for the Amazon CloudFront (CloudFront) distribution you specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableCloudFrontAccessLogs "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableCloudFrontAccessLogs")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf.

- BucketName

Type: String

Description: (Required) The name of the Amazon Simple Storage Service (Amazon S3) bucket you want to store
access logs in. Buckets in the af-south-1, ap-east-1, eu-south-1, and me-south-1
AWS Region are not supported.

- CloudFrontId

Type: String

Description: (Required) The ID of the CloudFront distribution you want to enable access
logging on.

- IncludeCookies

Type: Boolean

Valid values: true | false

Description: (Required) Set this parameter to `true` , if you want
cookies to be included in the access logs.

- Prefix

Type: String

Description: (Optional) An optional string that you want CloudFront to prefix to the
access log `filenames` for your distribution, for example,
`myprefix/`.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `cloudfront:GetDistribution`
- `cloudfront:GetDistributionConfig`
- `cloudfront:UpdateDistribution`
- `s3:GetBucketLocation`
- `s3:GetBucketAcl`
- `s3:PutBucketAcl`

###### Note

The `s3:GetBucketLocation` API can only be used for S3 buckets in same
account. You cannot use it for cross-account S3 buckets.

**Document Steps**

- `aws:executeScript` - Enables access logging for the CloudFront distribution
  you specify in the `CloudFrontDistributionId` parameter.
