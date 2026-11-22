

# `AWSSupportRemediator-BlockS3BucketPublicAccess`

**Description**

Disables all public access for the specified Amazon Simple Storage Service (Amazon S3) bucket.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon S3 Bucket Permissions](https://docs.aws.amazon.com/awssupport/latest/user/security-checks.html#amazon-s3-bucket-permissions) and AWS Security Hub CSPM controls [S3 general purpose buckets should block public read access](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-2), [S3 general purpose buckets should block public write access](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-3), and [S3 general purpose buckets should block public access](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-8).

If the Amazon S3 bucket does not exist or all public access is already disabled, the automation completes successfully without making changes.

Some buckets might intentionally allow public access, in which case running this runbook might cause availability issues.

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
+ BucketName

  Type: `AWS::S3::Bucket::Name`

  Description: (Required) The name of the Amazon S3 bucket for which to disable public access.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `s3:GetBucketPublicAccessBlock`
+ `s3:PutBucketPublicAccessBlock`

**Document Steps**

1. **validateInput** - Validates that the Amazon S3 bucket exists and checks the current public access block configuration.

1. **branchOnChangeRequired** - Branches on whether public access block configuration changes are required.

1. **blockS3PublicAccess** - Applies public access block configuration to disable all public access for the Amazon S3 bucket.

**Outputs**
+ validateInput.ChangeRequired: Whether a change is required.
+ validateInput.ValidationMessage: The reason if no change is required.
+ validateInput.PublicAccessBlockConfiguration: Initial public access block configuration of the Amazon S3 bucket before execution.