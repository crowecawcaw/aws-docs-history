# `AWS-AddWAFRegionalRuleToWebAcl`

**Description**

The `AWS-AddWAFRegionalRuleToWebAcl` runbook adds an existing AWS WAF
regional rule, rule group or rate-based rule to a AWS WAF Classic regional web access
control list (ACL). This runbook doesn't update existing AWS WAF Classic regional web
ACL’s that are managed by AWS Firewall Manager.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-AddWAFRegionalRuleToWebAcl "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-AddWAFRegionalRuleToWebAcl")

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

- WebACLId

Type: String

Description: (Required) The ID of the web ACL that you want to
update.

- ActivatedRulePriority

Type: Integer

Description: (Required) The priority for the new rule. Rule priority
determines the order in which rules in a web ACL are evaluated. Rules with a
lower value have higher priority than rules with a higher value. The value
must be a unique integer. If you add multiple rules to a regional web ACL,
the values don't have to be consecutive.

- ActivatedRuleRuleId

Type: String

Description: (Required) The ID for the regular rule, rate-based rule, or
group you want to add to the web ACL.

- ActivatedRuleAction

Type: String

Valid values: ALLOW | BLOCK | COUNT

Description: (Optional) Specifies the action that AWS WAF takes when a web
request matches the conditions of the rule.

- ActivatedRuleType

Type: String

Valid values: REGULAR | RATE_BASED | GROUP

Default: REGULAR

Description: (Optional) The rule type you're adding to the web ACL.
Although this field is optional, note that if you try to add a
`RATE_BASED` rule to a web ACL without setting the type, the
request fails because the request defaults to a `REGULAR`
rule.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `waf-regional:GetChangeToken`
- `waf-regional:GetWebACL`
- `waf-regional:UpdateWebACL`

**Document Steps**

- DetermineWebACLNotInFMSAndRulePriority (aws:executeScript) - Verifies if
  the AWS WAF web ACL is in a Firewall Manager security policy and verifies the priority ID
  doesn't conflict with an existing ACL.
- AddRuleOrRuleGroupToWebACL (aws:executeScript) - Adds the specified rule
  to the AWS WAF web ACL.
- VerifyRuleOrRuleGroupAddedToWebAcl (aws:executeScript) - Verifies the
  specified AWS WAF rule was added to the target web ACL.

**Outputs**

- DetermineWebACLNotInFMSAndRulePriority.PrereqResponse: Output from the
  `DetermineWebACLNotInFMSAndRulePriority` step.
- VerifyRuleOrRuleGroupAddedToWebAcl.VerifyRuleOrRuleGroupAddedToWebACLResponse:
  Output from the `AddRuleOrRuleGroupToWebACL` step.
- VerifyRuleOrRuleGroupAddedToWebAcl.ListActivatedRulesOrRuleGroupsInWebACLResponse:
  Output of the `VerifyRuleOrRuleGroupAddedToWebAcl` step.
