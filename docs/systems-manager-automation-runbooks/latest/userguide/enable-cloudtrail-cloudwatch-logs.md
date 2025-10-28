# `AWS-EnableCloudTrailCloudWatchLogs`

**Description**

This runbook updates the configuration of one or more AWS CloudTrail trails to send events to an Amazon CloudWatch Logs log group.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCloudTrailCloudWatchLogs "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCloudTrailCloudWatchLogs")

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

- CloudWatchLogsLogGroupArn

Type: String

Description: (Required) The ARN of the CloudWatch Logs log group where the CloudTrail logs will be delivered.

- CloudWatchLogsRoleArn

Type: String

Description: (Required) The ARN of the IAM role CloudWatch Logs Logs assumes to write to the specified log group.

- TrailNames

Type: StringList

Description: (Required) A comma separated list of the names of the CloudTrail trails whose events you want to send to CloudWatch Logs.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudtrail:UpdateTrail`
- `iam:PassRole`
  **Document Steps**

- `aws:executeScript` - Updates the specified CloudTrail trails to deliver events to the specified CloudWatch Logs log group.
