# `AWS-EnableCloudTrailLogFileValidation`

**Description**

The `AWS-EnableCloudTrailLogFileValidation` runbook enables log
file validation for the AWS CloudTrail trails you specify.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCloudTrailLogFileValidation "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCloudTrailLogFileValidation")

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

- TrailNames

Type: StringList

Description: (Required) A comma separated list of the names of the
CloudTrail trails you want to enable log validation for.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudtrail:GetTrail`
- `cloudtrail:UpdateTrail`
  **Document Steps**

- `aws:executeScript` - Enables log validation for the AWS CloudTrail trails you
  specify in the `TrailNames` parameter.
