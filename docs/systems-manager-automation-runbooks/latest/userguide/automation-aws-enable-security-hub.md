# `AWSConfigRemediation-EnableSecurityHub`

**Description**

The `AWSConfigRemediation-EnableSecurityHub` runbook enables AWS Security Hub CSPM
(Security Hub CSPM) for the AWS account and AWS Region where you run the automation. For
information about Security Hub CSPM, see [What is AWS Security Hub CSPM?](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") in the _AWS Security Hub CSPM User Guide_ .

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableSecurityHub "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableSecurityHub")

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

- EnableDefaultStandards

Type: Boolean

Default: true

Description: (Required) If set to `true` , the default
security standards designated by Security Hub CSPM are enabled.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `securityhub:DescribeHub`
- `securityhub:EnableSecurityHub`
- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`

**Document Steps**

- `aws:executeAwsApi` - Enables Security Hub CSPM in the current account and
  Region.
- `aws:executeAwsApi` - Verifies that Security Hub CSPM has been enabled.
