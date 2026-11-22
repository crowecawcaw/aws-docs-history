

# `AWSSupportRemediator-EnableCloudFrontDistributionLogging`

**Description**

Enables standard logging (legacy) for an Amazon CloudFront (CloudFront) distribution.

The runbook resolves the target Amazon Simple Storage Service (Amazon S3) logging bucket using a tag key and tag value pair, validates that the bucket meets the CloudFront standard logging (legacy) prerequisites, and then updates the CloudFront distribution configuration to enable logging.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [CloudFront distributions should have logging enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-5).

If the CloudFront distribution does not exist, or standard logging is already enabled on the CloudFront distribution, the automation completes successfully without making changes.

This runbook only configures the standard logging (legacy) required by the scope of the check; it does not configure standard logging v2 (vended logs to Amazon CloudWatch Logs, Amazon Data Firehose, or Amazon S3).

The tag-based bucket lookup supports centralized remediation across AWS Organizations. The delegated administrator holds a single parameter set and each member account tags its designated CloudFront logging bucket with the same tag pair. Exactly one Amazon S3 bucket in the account must be tagged with the `TargetBucketTagKey` and `TargetBucketTagValue` pair. The automation fails if zero or more than one bucket matches.

The target Amazon S3 bucket must have Amazon S3 Object Ownership set to a value other than `BucketOwnerEnforced`. That setting disables access control lists (ACLs), which CloudFront requires to deliver log files. The bucket ACL must also grant CloudFront (the `awslogsdelivery` account) `FULL_CONTROL` permission. The automation validates both prerequisites and fails with a descriptive error if either is missing. For more information about standard logging prerequisites, see [Configure standard logging (legacy)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/standard-logging-legacy-s3.html).

CloudFront writes log files to the bucket, which incur Amazon S3 storage charges. For more information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

CloudFront distribution updates can take up to 15 minutes to propagate to all edge locations. The automation returns as soon as the `UpdateDistribution` API call is accepted, and log files begin arriving after propagation completes.

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
+ DistributionId

  Type: String

  Description: (Required) The ID of the CloudFront distribution.
+ IncludeCookies

  Type: Boolean

  Description: (Required) Whether to include cookies in CloudFront access logs.
+ S3KeyPrefix

  Type: String

  Description: (Required) The prefix for the log file location in the target Amazon S3 bucket, for example `accesslogs/cloudfront/`.
+ TargetBucketTagKey

  Type: String

  Description: (Required) The tag key (case-sensitive) used to identify the target Amazon S3 bucket for CloudFront distribution logging.
+ TargetBucketTagValue

  Type: String

  Description: (Required) The tag value (case-sensitive) used to identify the target Amazon S3 bucket for CloudFront distribution logging.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudfront:GetDistribution`
+ `cloudfront:UpdateDistribution`
+ `s3:GetBucketAcl`
+ `s3:GetBucketOwnershipControls`
+ `tag:GetResources`

**Document Steps**

1. **validateInput** - Resolves the target Amazon S3 bucket from the provided tag pair. Validates that the bucket meets CloudFront standard logging (legacy) prerequisites. Determines whether standard logging needs to be enabled on the CloudFront distribution. Reports no change required if the distribution does not exist or logging is already enabled.

1. **branchOnChangeRequired** - Branches on whether a change to the CloudFront distribution logging configuration is required. Ends the automation successfully when no change is needed.

1. **enableCloudFrontDistributionLogging** - Enables standard logging on the CloudFront distribution by updating the distribution configuration to write access logs to the resolved Amazon S3 bucket.

**Outputs**
+ validateInput.TargetBucket: The name of the Amazon S3 bucket used as the CloudFront logging destination.
+ validateInput.ChangeRequired: Whether a change to the CloudFront distribution logging configuration is required.
+ validateInput.ValidationMessage: The reason when no change is required.
+ enableCloudFrontDistributionLogging.InitialLoggingConfig: The pre-change `Logging` block of the CloudFront distribution configuration, captured for rollback. Use this output value to manually restore the prior logging configuration via UpdateDistribution if needed. Present only when a change is made.