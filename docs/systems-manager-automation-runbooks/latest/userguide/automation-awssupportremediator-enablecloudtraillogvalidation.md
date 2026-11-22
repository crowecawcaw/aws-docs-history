

# `AWSSupportRemediator-EnableCloudTrailLogValidation`

**Description**

Enables log file validation for an AWS CloudTrail trail.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [CloudTrail log file validation should be enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-4).

If the CloudTrail trail does not exist or log file validation is already enabled, the automation completes successfully without making changes.

To disable log file validation after enabling, modify the trail configuration manually.

Log file validation produces one digest file per hour that is stored in the same Amazon Simple Storage Service (Amazon S3) bucket as the CloudTrail logs. For more information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

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
+ TrailArn

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the CloudTrail trail on which to enable log file validation.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudtrail:GetTrail`
+ `cloudtrail:UpdateTrail`

**Document Steps**

1. **validateTrail** - Validates whether the CloudTrail trail exists and whether log file validation is already enabled.

1. **branchOnChangeRequired** - Branches on whether log file validation needs to be enabled.

1. **updateTrailLogValidation** - Enables log file validation on the CloudTrail trail.

**Outputs**
+ validateTrail.ChangeRequired: Whether log file validation needs to be enabled on the CloudTrail trail.
+ validateTrail.TrailLogValidationInitiallyEnabled: Whether log file validation is already enabled on the CloudTrail trail.
+ validateTrail.ValidationMessage: A message describing the validation result.