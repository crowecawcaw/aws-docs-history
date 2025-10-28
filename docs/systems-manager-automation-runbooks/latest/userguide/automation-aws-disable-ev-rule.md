# `AWS-DisableEventBridgeRule`

**Description**

The `AWS-DisableEventBridgeRule` runbook disables the Amazon EventBridge rule
you specify.To learn more about EventBridge rules, see [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the
_Amazon EventBridge User Guide_ .

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DisableEventBridgeRule "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DisableEventBridgeRule")

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

- EventBusName

Type: String

Default: default

Description: (Optional) The event bus associated with the rule you want to
disable.

- RuleName

Type: String

Description: (Required) The name of the rule you want to disable.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `events:DisableRule`

**Document Steps**

- `aws:executeAwsApi` - Disables the EventBridge rule you specify in the
  `RuleName` parameter.
