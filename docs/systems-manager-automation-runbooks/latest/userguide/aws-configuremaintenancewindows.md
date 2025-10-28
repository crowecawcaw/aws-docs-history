# `AWS-ConfigureMaintenanceWindows`

**Description**

The `AWS-ConfigureMaintenanceWindows` runbook helps you to enable or
disable multiple Systems Manager maintenance windows.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ConfigureMaintenanceWindows "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ConfigureMaintenanceWindows")

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

- MaintenanceWindows

Type: StringList

Description: (Required) A comma-separated list of the IDs of the
maintenance windows you want to enable or disable.

- MaintenanceWindowsStatus

Type: String

Valid values: "True" | "False"

Default: "False"

Description: (Required) Determines whether maintenance windows are enabled
or disabled. Specify "True" to enable maintenance windows, and "False" to
disable them.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetMaintenanceWindow`
- `ssm:UpdateMaintenanceWindow`

**Document Steps**

- `aws:executeScript` - Gathers the status of the maintenance
  windows you specify in the `MaintenanceWindows` parameter, and
  enables or disables the maintenance windows.
