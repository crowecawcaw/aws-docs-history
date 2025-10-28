# `AWS-AddWAFRegionalRuleToRuleGroup`

**Description**

The `AWS-AddWAFRegionalRuleToRuleGroup` runbook adds an existing AWS WAF
regional rule to a AWS WAF regional rule group. Only AWS WAF Classic regional rule
groups are supported. AWS WAF Classic regional rule groups can have a maximum of 10
rules.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-AddWAFRegionalRuleToRuleGroup "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-AddWAFRegionalRuleToRuleGroup")

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

- RuleGroupId

Type: String

Description: (Required) The ID of the rule group that you want to
update.

- RulePriority

Type: Integer

Description: (Required) The priority for the new rule. Rule priority
determines the order in which rules in a regional group are evaluated. Rules
with a lower value have higher priority than rules with a higher value. The
value must be a unique integer. If you add multiple rules to a regional rule
group, the values don't have to be consecutive.

- RuleId

Type: String

Description: (Required) The ID for the rule that you want to add to your
regional rule group.

- RuleAction

Type: String

Description: (Required) Specifies the action that AWS WAF takes when a web
request matches the conditions of the rule.

Valid values: ALLOW | BLOCK | COUNT
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `waf-regional:GetChangeToken`
- `waf-regional:GetChangeTokenStatus`
- `waf-regional:ListActivatedRulesInRuleGroup`
- `waf-regional:UpdateRuleGroup`

**Document Steps**

- GetWAFChangeToken (aws:executeAwsApi) - Retrieves a AWS WAF change token to
  ensure the runbook doesn't submit conflicting requests to the
  service.
- AddWAFRuleToWAFRegionalRuleGroup (aws:executeScript) - Adds the specified
  rule to the AWS WAF regional rule group.
- VerifyChangeTokenPropagating (aws:waitForAwsResourceProperty) - Verifies
  the change token has a status of `PENDING` or
  `INSYNC`.
- VerifyRuleAddedToRuleGroup (aws:executeScript) - Verifies the specified
  AWS WAF rule was added to the target regional rule group.

**Outputs**

- VerifyRuleAddedToRuleGroup.VerifyRuleAddedToRuleGroupResponse - Output of
  the step verifying that the new rule was aded to the regional rule
  group.
- VerifyRuleAddedToRuleGroup.ListActivatedRulesInRuleGroupResponse - Output
  of the `ListActivatedRulesInRuleGroup` API operation.
