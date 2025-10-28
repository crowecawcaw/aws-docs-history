# `AWSConfigRemediation-EnableCloudTrailLogFileValidation`

**Description**

The
`AWSConfigRemediation-EnableCloudTrailLogFileValidation`
runbook
enables log file validation for your AWS CloudTrail trail.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableCloudTrailLogFileValidation "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableCloudTrailLogFileValidation")

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

- TrailName

Type: String

Description: (Required) The name or Amazon Resource Name (ARN) of the
trail you want to enable log validation for.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `cloudtrail:GetTrail`
- `cloudtrail:UpdateTrail`

**Document Steps**

- `aws:executeAwsApi`

* Enables log validation for the AWS CloudTrail
  trail you specify in the
  `TrailName`
  parameter.

- `aws:assertAwsResourceProperty`

* Verifies log validation is
  enabled for your trail.
