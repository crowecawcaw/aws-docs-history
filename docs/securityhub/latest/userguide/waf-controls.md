# Security Hub CSPM controls for AWS WAF

These AWS Security Hub CSPM controls evaluate the AWS WAF service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [WAF.1] AWS WAF Classic Global Web ACL logging should be enabled

**Related requirements:** NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::WAF::WebACL`

**AWS Config rule:**
[`waf-classic-logging-enabled`](../../../config/latest/developerguide/waf-classic-logging-enabled.md "../../../config/latest/developerguide/waf-classic-logging-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether logging is enabled for an AWS WAF global web ACL. This
control fails if logging is not enabled for the web ACL.

Logging is an important part of maintaining the reliability, availability, and
performance of AWS WAF globally. It is a business and compliance requirement in many
organizations, and allows you to troubleshoot application behavior. It also provides
detailed information about the traffic that is analyzed by the web ACL that is
attached to AWS WAF.

### Remediation

To enable logging for an AWS WAF web ACL, see [Logging web ACL traffic information](../../../waf/latest/developerguide/classic-logging.md "../../../waf/latest/developerguide/classic-logging.md") in the _AWS WAF Developer Guide_.

## [WAF.2] AWS WAF Classic Regional rules should have at least one condition

**Related requirements:** NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21)

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:**
`AWS::WAFRegional::Rule`

**AWS Config rule:**
[`waf-regional-rule-not-empty`](../../../config/latest/developerguide/waf-regional-rule-not-empty.md "../../../config/latest/developerguide/waf-regional-rule-not-empty.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF Regional rule has at least one condition. The control fails if no conditions are present within a rule.

A WAF Regional rule can contain multiple conditions. The rule's conditions allow for traffic inspection and take a defined action (allow, block, or count).
Without any conditions, the traffic passes without inspection. A WAF Regional rule with no conditions, but with a name or tag suggesting allow, block, or count, could
lead to the wrong assumption that one of those actions is occurring.

### Remediation

To add a condition to an empty rule, see [Adding and removing conditions in a rule](../../../waf/latest/developerguide/classic-web-acl-rules-editing.md "../../../waf/latest/developerguide/classic-web-acl-rules-editing.md") in the _AWS WAF Developer Guide_.

## [WAF.3] AWS WAF Classic Regional rule groups should have at least one rule

**Related requirements:** NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21)

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:**
`AWS::WAFRegional::RuleGroup`

**AWS Config rule:**
[`waf-regional-rulegroup-not-empty`](../../../config/latest/developerguide/waf-regional-rulegroup-not-empty.md "../../../config/latest/developerguide/waf-regional-rulegroup-not-empty.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF Regional rule group has at least one rule. The control fails if no rules are present within a rule group.

A WAF Regional rule group can contain multiple rules. The rule's conditions allow for traffic inspection and take a defined action (allow, block, or count).
Without any rules, the traffic passes without inspection. A WAF Regional rule group with no rules, but with a name or tag suggesting allow, block, or count, could
lead to the wrong assumption that one of those actions is occurring.

### Remediation

To add rules and rule conditions to an empty rule group, see [Adding and deleting rules from an AWS WAF Classic rule group](../../../waf/latest/developerguide/classic-rule-group-editing.md "../../../waf/latest/developerguide/classic-rule-group-editing.md")
and [Adding and removing conditions in a rule](../../../waf/latest/developerguide/classic-web-acl-rules-editing.md "../../../waf/latest/developerguide/classic-web-acl-rules-editing.md") in the _AWS WAF Developer Guide_.

## [WAF.4] AWS WAF Classic Regional web ACLs should have at least one rule or rule group

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:**
`AWS::WAFRegional::WebACL`

**AWS Config rule:**
[`waf-regional-webacl-not-empty`](../../../config/latest/developerguide/waf-regional-webacl-not-empty.md "../../../config/latest/developerguide/waf-regional-webacl-not-empty.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF Classic Regional web ACL contains any WAF rules or WAF rule groups. This control fails if a web ACL does not contain any
WAF rules or rule groups.

A WAF Regional web ACL can contain a collection of rules and rule groups that inspect and control web requests. If a web ACL is empty, the web traffic can
pass without being detected or acted upon by WAF depending on the default action.

### Remediation

To add rules or rule groups to an empty AWS WAF Classic Regional web ACL, see [Editing a Web ACL](../../../waf/latest/developerguide/classic-web-acl-editing.md "../../../waf/latest/developerguide/classic-web-acl-editing.md") in the _AWS WAF Developer Guide_.

## [WAF.6] AWS WAF Classic global rules should have at least one condition

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:**
`AWS::WAF::Rule`

**AWS Config rule:**
[`waf-global-rule-not-empty`](../../../config/latest/developerguide/waf-global-rule-not-empty.md "../../../config/latest/developerguide/waf-global-rule-not-empty.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF global rule contains any conditions. The control fails if no conditions are present within a rule.

A WAF global rule can contain multiple conditions. A rule's conditions allow for traffic inspection and take a defined action (allow, block, or count).
Without any conditions, the traffic passes without inspection. A WAF global rule with no conditions, but with a name or tag suggesting allow, block, or count, could
lead to the wrong assumption that one of those actions is occurring.

### Remediation

For instructions on creating a rule and adding conditions, see [Creating a rule and adding conditions](../../../waf/latest/developerguide/classic-web-acl-rules-creating.md "../../../waf/latest/developerguide/classic-web-acl-rules-creating.md") in the _AWS WAF Developer Guide_.

## [WAF.7] AWS WAF Classic global rule groups should have at least one rule

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:**
`AWS::WAF::RuleGroup`

**AWS Config rule:**
[`waf-global-rulegroup-not-empty`](../../../config/latest/developerguide/waf-global-rulegroup-not-empty.md "../../../config/latest/developerguide/waf-global-rulegroup-not-empty.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF global rule group has at least one rule. The control fails if no rules are present within a rule group.

A WAF global rule group can contain multiple rules. The rule's conditions allow for traffic inspection and take a defined action (allow, block, or count).
Without any rules, the traffic passes without inspection. A WAF global rule group with no rules, but with a name or tag suggesting allow, block, or count, could
lead to the wrong assumption that one of those actions is occurring.

### Remediation

For instructions on adding a rule to a rule group, see [Creating an AWS WAF Classic rule group](../../../waf/latest/developerguide/classic-create-rule-group.md "../../../waf/latest/developerguide/classic-create-rule-group.md") in the _AWS WAF Developer Guide_.

## [WAF.8] AWS WAF Classic global web ACLs should have at least one rule or rule group

**Related requirements:** NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21)

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:**
`AWS::WAF::WebACL`

**AWS Config rule:**
[`waf-global-webacl-not-empty`](../../../config/latest/developerguide/waf-global-webacl-not-empty.md "../../../config/latest/developerguide/waf-global-webacl-not-empty.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF global web ACL contains at least one WAF rule or WAF rule group. The control fails if a web ACL does not contain any
WAF rules or rule groups.

A WAF global web ACL can contain a collection of rules and rule groups that inspect and control web requests. If a web ACL is empty, the web traffic can
pass without being detected or acted upon by WAF depending on the default action.

### Remediation

To add rules or rule groups to an empty AWS WAF global web ACL, see [Editing a web ACL](../../../waf/latest/developerguide/classic-web-acl-editing.md "../../../waf/latest/developerguide/classic-web-acl-editing.md")
in the _AWS WAF Developer Guide_. For **Filter**, choose **Global (CloudFront)**.

## [WAF.10] AWS WAF web ACLs should have at least one rule or rule group

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:**
`AWS::WAFv2::WebACL`

**AWS Config rule:**
[`wafv2-webacl-not-empty`](../../../config/latest/developerguide/wafv2-webacl-not-empty.md "../../../config/latest/developerguide/wafv2-webacl-not-empty.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAFV2 web access control list (web ACL) contains at least one
rule or rule group. The control fails if a web ACL does not contain any rules or rule groups.

A web ACL gives you fine-grained control over all of the HTTP(S) web requests that your protected resource responds to.
A web ACL should contain a collection of rules and rule groups that inspect and control web requests. If a web ACL is empty,
the web traffic can pass without being detected or acted upon by AWS WAF depending on the default action.

### Remediation

To add rules or rule groups to an empty WAFV2 web ACL, see [Editing a Web ACL](../../../waf/latest/developerguide/web-acl-editing.md "../../../waf/latest/developerguide/web-acl-editing.md") in the _AWS WAF Developer Guide_.

## [WAF.11] AWS WAF web ACL logging should be enabled

**Related requirements:** NIST.800-53.r5 AC-4(26),
NIST.800-53.r5 AU-10,
NIST.800-53.r5 AU-12,
NIST.800-53.r5 AU-2,
NIST.800-53.r5 AU-3,
NIST.800-53.r5 AU-6(3),
NIST.800-53.r5 AU-6(4),
NIST.800-53.r5 CA-7,
NIST.800-53.r5 SC-7(10),
NIST.800-53.r5 SC-7(9),
NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Low

**Resource type:**
`AWS::WAFv2::WebACL`

**AWS Config rule:**
[`wafv2-logging-enabled`](../../../config/latest/developerguide/wafv2-logging-enabled.md "../../../config/latest/developerguide/wafv2-logging-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether logging is activated for an AWS WAFV2 web access control list (web ACL). This control
fails if logging is deactivated for the web ACL.

###### Note

This control doesn't check whether AWS WAF web ACL logging is enabled for an account through Amazon Security Lake.

Logging maintains the reliability, availability, and performance of AWS WAF. In addition, logging is a business and
compliance requirement in many organizations. By logging traffic that's analyzed by your web ACL, you can troubleshoot
application behavior.

### Remediation

To activate logging for an AWS WAF web ACL, see [Managing logging for a web ACL](../../../waf/latest/developerguide/logging-management.md "../../../waf/latest/developerguide/logging-management.md") in the
_AWS WAF Developer Guide_.

## [WAF.12] AWS WAF rules should have CloudWatch metrics enabled

**Related requirements:** NIST.800-53.r5 AC-4(26),
NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3,
NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5
SC-7(10), NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-7(8), NIST.800-171.r2 3.14.6,
NIST.800-171.r2 3.14.7

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::WAFv2::RuleGroup`

**AWS Config rule:**
[`wafv2-rulegroup-logging-enabled`](../../../config/latest/developerguide/wafv2-rulegroup-logging-enabled.md "../../../config/latest/developerguide/wafv2-rulegroup-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF rule or rule group has Amazon CloudWatch metrics enabled. The control fails if the rule or
rule group doesn't have CloudWatch metrics enabled.

Configuring CloudWatch metrics on AWS WAF rules and rule groups provides visibility into traffic flow. You can see which
ACL rules are triggered and which requests are accepted and blocked. This visibility can help you identify malicious activity on
your associated resources.

### Remediation

To enable CloudWatch metrics on an AWS WAF rule group, invoke the [UpdateRuleGroup](../../../waf/latest/APIReference/API_UpdateRuleGroup.md "../../../waf/latest/APIReference/API_UpdateRuleGroup.md") API. To enable CloudWatch metrics on an AWS WAF rule, invoke the [UpdateWebACL](../../../waf/latest/APIReference/API_UpdateWebACL.md "../../../waf/latest/APIReference/API_UpdateWebACL.md") API. Set the `CloudWatchMetricsEnabled` field to `true`. When you use the AWS WAF console to create
rules or rule groups, CloudWatch metrics are automatically enabled.
