

# `AWSSupportRemediator-EnableS3AbortIncompleteMultipartUpload`

**Description**

Creates or updates a lifecycle rule on an Amazon Simple Storage Service (Amazon S3) bucket to abort incomplete multipart uploads after a specified number of days.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Trusted Advisor check [Amazon S3 Incomplete Multipart Upload Abort Configuration](https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html#s3-incomplete-multipart-upload-abort-config).

If the Amazon S3 bucket does not exist or already has an abort incomplete multipart upload lifecycle rule for all objects with `DaysAfterInitiation` less than or equal to 7, the automation completes successfully without making changes.

If the bucket has no lifecycle configuration, the automation creates one with the abort incomplete multipart upload rule. If the bucket has an existing lifecycle configuration without an abort rule for all objects, or with `DaysAfterInitiation` greater than 7, the automation appends the rule to the existing configuration.

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
+ BucketArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the Amazon S3 bucket on which to configure the abort incomplete multipart upload lifecycle rule.
+ DaysAfterInitiation

  Type: Integer

  Description: (Optional) The number of days after which Amazon S3 aborts an incomplete multipart upload. Valid range is 1 to 7.

  Default: 7

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `s3:GetLifecycleConfiguration`
+ `s3:PutLifecycleConfiguration`

**Document Steps**

1. **validateRequest** - Validates the Amazon S3 bucket and determines whether the abort incomplete multipart upload lifecycle rule needs to be created or updated.

1. **branchOnChangeRequired** - Branches on whether the lifecycle configuration change is needed.

1. **buildLifecycleConfiguration** - Builds the new lifecycle configuration by appending the abort incomplete multipart upload rule to the existing rules.

1. **putLifecycleConfiguration** - Updates the Amazon S3 bucket lifecycle configuration with the new abort incomplete multipart upload rule.

1. **getFinalLifecycleConfiguration** - Retrieves the final lifecycle configuration of the Amazon S3 bucket after the update.

**Outputs**
+ validateRequest.InitialRules: The initial lifecycle configuration rules of the Amazon S3 bucket.
+ validateRequest.ValidationMessage: A message describing the validation result.
+ validateRequest.ChangeRequired: Whether the remediation is required.
+ getFinalLifecycleConfiguration.Rules: The final lifecycle configuration rules of the Amazon S3 bucket.