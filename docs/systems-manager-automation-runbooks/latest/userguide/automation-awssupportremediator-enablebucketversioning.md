

# `AWSSupportRemediator-EnableBucketVersioning`

**Description**

Enables versioning for an Amazon Simple Storage Service (Amazon S3) bucket.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon S3 Bucket Versioning](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-s3-bucket-versioning).

If the bucket does not exist or versioning is already enabled, the automation completes successfully without making changes.

To suspend versioning after enabling, modify the bucket versioning configuration to `Suspended`. Amazon S3 retains existing versioned objects even after you suspend versioning.

Enabling versioning might increase Amazon S3 storage costs because Amazon S3 retains all object versions. For more information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

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

  Description: (Required) The name of the Amazon S3 bucket on which to enable versioning.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `s3:GetBucketVersioning`
+ `s3:PutBucketVersioning`

**Document Steps**

1. **validateBucket** - Validates that the Amazon S3 bucket exists and checks its current versioning status.

1. **branchOnChangeRequired** - Branches on whether versioning needs to be enabled.

1. **enableBucketVersioning** - Enables versioning for the Amazon S3 bucket.

**Outputs**
+ validateBucket.ChangeRequired: Whether bucket versioning needs to be enabled.
+ validateBucket.ValidationMessage: Information about the validation result.
+ validateBucket.InitialBucketVersioningStatus: The initial versioning status of the bucket.