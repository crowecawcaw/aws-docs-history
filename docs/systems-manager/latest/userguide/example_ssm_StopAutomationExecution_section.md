AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `StopAutomationExecution` with a CLI

The following code examples show how to use `StopAutomationExecution`.

CLI

**AWS CLI**

**To stop an automation execution**

The following `stop-automation-execution` example stops an Automation document.

```
`aws ssm stop-automation-execution
 --automation-execution-id `"4105a4fc-f944-11e6-9d32-0a1b2EXAMPLE"``

```

This command produces no output.

For more information, see [Running an Automation Workflow Manually](automation-working-executing-manually.md "automation-working-executing-manually.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [StopAutomationExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/stop-automation-execution.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/stop-automation-execution.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example stops an Automation Execution. There is no output if the command succeeds.**

```
Stop-SSMAutomationExecution -AutomationExecutionId "4105a4fc-f944-11e6-9d32-8fb2db27a909"

```

- For API details, see
  [StopAutomationExecution](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example stops an Automation Execution. There is no output if the command succeeds.**

```
Stop-SSMAutomationExecution -AutomationExecutionId "4105a4fc-f944-11e6-9d32-8fb2db27a909"

```

- For API details, see
  [StopAutomationExecution](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
