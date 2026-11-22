

# `AWSSupportRemediator-EnableBucketAccessLogging`

**Description**

Enables server access logging for the specified Amazon Simple Storage Service (Amazon S3) bucket.

The runbook identifies the destination bucket by the tag key and value you provide. It uses the source bucket name as the target prefix in the destination bucket.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [S3 general purpose buckets should have server access logging enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-9).

If the Amazon S3 bucket does not exist or server access logging is already enabled, the automation completes successfully without making changes.

Before running this automation, verify that the destination bucket meets all of the following requirements:
+ The destination bucket must be in the same AWS Region and AWS account as the source bucket.
+ Enable [Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) at the account or bucket level, with all four settings enabled.
+ Configure the destination bucket to receive Amazon S3 server access logs. For more information, see [Permissions for log delivery](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html#grant-log-delivery-permissions-general).

The automation fails without making changes if zero or more than one bucket matches the provided tag pair. It also fails if the destination bucket is the same as the source bucket. The automation also fails if the destination bucket does not have all four Amazon S3 Block Public Access settings enabled.

Log objects are stored in the destination bucket and incur Amazon S3 storage cost. For more information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

To disable server access logging after enabling, modify the bucket logging configuration to remove the logging destination.

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

  Description: (Required) The name of the Amazon S3 bucket for which to enable server access logging.
+ TargetBucketTagKey

  Type: String

  Description: (Required) The tag key (case-sensitive) used to identify the destination Amazon S3 bucket. Use this with `TargetBucketTagValue` to tag the bucket to be used as the destination bucket for access logging.
+ TargetBucketTagValue

  Type: String

  Description: (Required) The tag value (case-sensitive) used to identify the destination Amazon S3 bucket. Use this with `TargetBucketTagKey` to tag the bucket to be used as the destination bucket for access logging.
+ TargetObjectKeyFormat

  Type: String

  Description: (Optional) The Amazon S3 key format for log objects. Use `SimplePrefix` for the simple format, `PartitionedPrefixEventTime` for partitioned prefix with event time, or `PartitionedPrefixDeliveryTime` for partitioned prefix with delivery time.

  Default: PartitionedPrefixEventTime

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `s3:GetAccountPublicAccessBlock`
+ `s3:GetBucketLocation`
+ `s3:GetBucketLogging`
+ `s3:GetBucketPublicAccessBlock`
+ `s3:PutBucketLogging`
+ `tag:GetResources`

**Document Steps**

1. **retrieveTargetBucketName** - Retrieves the name of the destination Amazon S3 bucket by looking up resources tagged with `TargetBucketTagKey` and `TargetBucketTagValue`. Fails if zero or more than one Amazon S3 bucket matches the tag pair. Also fails if the destination bucket is the same as the source bucket.

1. **validateAccessLoggingRequest** - Validates that the source Amazon S3 bucket exists and that server access logging is not already enabled. Verifies that the destination bucket is in the same AWS Region. Confirms that the destination bucket has all four Amazon S3 Block Public Access settings enabled at either the account or bucket level. Returns the target object key format configuration used by the `enableS3Logging` step.

1. **branchOnChangeRequired** - Branches on whether server access logging changes are required.

1. **enableS3Logging** - Enables server access logging on the source Amazon S3 bucket, delivering logs to the destination bucket with the source bucket name as the target prefix.

**Outputs**
+ retrieveTargetBucketName.TargetBucket: The name of the destination Amazon S3 bucket.
+ validateAccessLoggingRequest.ChangeRequired: Whether server access logging changes are required.
+ validateAccessLoggingRequest.ValidationMessage: A message describing the validation result.