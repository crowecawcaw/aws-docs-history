

# `AWSSupportRemediator-IntegrateCloudTrailWithCloudWatch`

**Description**

Configures an AWS CloudTrail trail to deliver log files to an Amazon CloudWatch Logs log group.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [CloudTrail trails should be integrated with Amazon CloudWatch Logs](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-5).

If the CloudTrail trail does not exist or already delivers log files to a CloudWatch Logs log group, the automation completes successfully without making changes. The automation does not update a trail that already delivers log files to a different CloudWatch Logs log group than `CloudWatchLogsLogGroupName`.

The CloudWatch Logs log group specified by `CloudWatchLogsLogGroupName` must exist in the same account and AWS Region as the trail. The IAM role specified by `CloudWatchLogsRoleName` must exist in your account. The role must have a trust policy allowing `cloudtrail.amazonaws.com` to assume it and permissions to write to the log group.

Enabling CloudWatch Logs integration causes CloudTrail to continuously deliver log files to the specified log group. This incurs CloudWatch Logs ingestion and storage charges in your account. For more information about pricing, see [Amazon CloudWatch Logs pricing](https://aws.amazon.com/cloudwatch/pricing/).

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
+ CloudWatchLogsLogGroupName

  Type: String

  Description: (Required) The name of the CloudWatch Logs log group that receives the CloudTrail log files. The log group must exist in the same account and AWS Region as the trail.
+ CloudWatchLogsRoleName

  Type: String

  Description: (Required) The name of the IAM role that CloudTrail assumes to write to the CloudWatch Logs log group. The role must exist in your account.
+ TrailName

  Type: String

  Description: (Required) The name of the CloudTrail trail.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudtrail:DescribeTrails`
+ `cloudtrail:UpdateTrail`
+ `iam:PassRole`

**Document Steps**

1. **validateTrail** - Validates whether the CloudTrail trail requires integration with CloudWatch Logs. Returns `ChangeRequired: False` when the trail does not exist or already delivers log files to a CloudWatch Logs log group.

1. **branchOnTrailStatus** - Branches on whether the CloudTrail trail requires a change. Ends the automation successfully when the trail does not require a change, otherwise continues to `updateTrail`.

1. **updateTrail** - Invokes the CloudTrail `UpdateTrail` API to configure the CloudTrail trail to deliver log files to the specified CloudWatch Logs log group. Uses the specified IAM role.

**Outputs**
+ validateTrail.ChangeRequired: Whether the CloudTrail trail requires a configuration change.
+ validateTrail.ValidationMessage: The validation outcome message describing why a change is or is not required.