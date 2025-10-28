# `AWS-AddOpsItemDedupStringToEventBridgeRule`

**Description**

The `AWS-AddOpsItemDedupStringToEventBridgeRule` runbook adds a
deduplication string for all AWS Systems Manager OpsItems associated with an Amazon EventBridge rule. The
runbook doesn't add a deduplication string to the rule if one has already been
applied. To learn more deduplication strings and OpsItems, see [Reducing duplicate OpsItems](../../../systems-manager/latest/userguide/OpsCenter-creating-OpsItems.md#OpsCenter-working-deduplication "../../../systems-manager/latest/userguide/OpsCenter-creating-OpsItems.md#OpsCenter-working-deduplication") in the
_AWS Systems Manager User Guide_ .

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-AddOpsItemDedupStringToEventBridgeRule "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-AddOpsItemDedupStringToEventBridgeRule")

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

- DedupString

Type: String

Description: (Required) The deduplication string you want to add to the
rule.

- RuleName

Type: String

Description: (Required) The name of the rule you want to add the
deduplication string to.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `events:ListTargetsByRule`
- `events:PutTargets`

**Document Steps**

- `aws:executeScript` - Adds a deduplication string to the EventBridge
  rule you specify in the `RuleName` parameter.
