

# Security Hub CSPM controls for AWS WAF
<a name="waf-controls"></a>

These AWS Security Hub CSPM controls evaluate the AWS WAF service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [WAF.1] AWS WAF Classic Global Web ACL logging should be enabled
<a name="waf-1"></a>

**Related requirements:** NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::WAF::WebACL`

**AWS Config rule:** [`waf-classic-logging-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/waf-classic-logging-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether logging is enabled for an AWS WAF global web ACL. This control fails if logging is not enabled for the web ACL.

Logging is an important part of maintaining the reliability, availability, and performance of AWS WAF globally. It is a business and compliance requirement in many organizations, and allows you to troubleshoot application behavior. It also provides detailed information about the traffic that is analyzed by the web ACL that is attached to AWS WAF.

### Remediation
<a name="waf-1-remediation"></a>

To enable logging for an AWS WAF web ACL, see [ Logging web ACL traffic information](https://docs.aws.amazon.com/waf/latest/developerguide/classic-logging.html) in the *AWS WAF Developer Guide*.

## [WAF.2] AWS WAF Classic Regional rules should have at least one condition
<a name="waf-2"></a>

**Related requirements:** NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21)

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::WAFRegional::Rule`

**AWS Config rule:** [`waf-regional-rule-not-empty`](https://docs.aws.amazon.com/config/latest/developerguide/waf-regional-rule-not-empty.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF Regional rule has at least one condition. The control fails if no conditions are present within a rule.

A WAF Regional rule can contain multiple conditions. The rule's conditions allow for traffic inspection and take a defined action (allow, block, or count). Without any conditions, the traffic passes without inspection. A WAF Regional rule with no conditions, but with a name or tag suggesting allow, block, or count, could lead to the wrong assumption that one of those actions is occurring.

### Remediation
<a name="waf-2-remediation"></a>

To add a condition to an empty rule, see [Adding and removing conditions in a rule](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-editing.html) in the *AWS WAF Developer Guide*.

## [WAF.3] AWS WAF Classic Regional rule groups should have at least one rule
<a name="waf-3"></a>

**Related requirements:** NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21)

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::WAFRegional::RuleGroup`

**AWS Config rule:** [`waf-regional-rulegroup-not-empty`](https://docs.aws.amazon.com/config/latest/developerguide/waf-regional-rulegroup-not-empty.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF Regional rule group has at least one rule. The control fails if no rules are present within a rule group.

A WAF Regional rule group can contain multiple rules. The rule's conditions allow for traffic inspection and take a defined action (allow, block, or count). Without any rules, the traffic passes without inspection. A WAF Regional rule group with no rules, but with a name or tag suggesting allow, block, or count, could lead to the wrong assumption that one of those actions is occurring.

### Remediation
<a name="waf-3-remediation"></a>

To add rules and rule conditions to an empty rule group, see [Adding and deleting rules from an AWS WAF Classic rule group](https://docs.aws.amazon.com/waf/latest/developerguide/classic-rule-group-editing.html) and [Adding and removing conditions in a rule](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-editing.html) in the *AWS WAF Developer Guide*.

## [WAF.4] AWS WAF Classic Regional web ACLs should have at least one rule or rule group
<a name="waf-4"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::WAFRegional::WebACL`

**AWS Config rule:** [`waf-regional-webacl-not-empty`](https://docs.aws.amazon.com/config/latest/developerguide/waf-regional-webacl-not-empty)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF Classic Regional web ACL contains any WAF rules or WAF rule groups. This control fails if a web ACL does not contain any WAF rules or rule groups.

A WAF Regional web ACL can contain a collection of rules and rule groups that inspect and control web requests. If a web ACL is empty, the web traffic can pass without being detected or acted upon by WAF depending on the default action.

### Remediation
<a name="waf-4-remediation"></a>

To add rules or rule groups to an empty AWS WAF Classic Regional web ACL, see [Editing a Web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-editing.html) in the *AWS WAF Developer Guide*.

## [WAF.6] AWS WAF Classic global rules should have at least one condition
<a name="waf-6"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::WAF::Rule`

**AWS Config rule:** [`waf-global-rule-not-empty`](https://docs.aws.amazon.com/config/latest/developerguide/waf-global-rule-not-empty.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF global rule contains any conditions. The control fails if no conditions are present within a rule.

A WAF global rule can contain multiple conditions. A rule's conditions allow for traffic inspection and take a defined action (allow, block, or count). Without any conditions, the traffic passes without inspection. A WAF global rule with no conditions, but with a name or tag suggesting allow, block, or count, could lead to the wrong assumption that one of those actions is occurring.

### Remediation
<a name="waf-6-remediation"></a>

For instructions on creating a rule and adding conditions, see [Creating a rule and adding conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-creating.html) in the *AWS WAF Developer Guide*.

## [WAF.7] AWS WAF Classic global rule groups should have at least one rule
<a name="waf-7"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::WAF::RuleGroup`

**AWS Config rule:** [`waf-global-rulegroup-not-empty`](https://docs.aws.amazon.com/config/latest/developerguide/waf-global-rulegroup-not-empty.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF global rule group has at least one rule. The control fails if no rules are present within a rule group.

A WAF global rule group can contain multiple rules. The rule's conditions allow for traffic inspection and take a defined action (allow, block, or count). Without any rules, the traffic passes without inspection. A WAF global rule group with no rules, but with a name or tag suggesting allow, block, or count, could lead to the wrong assumption that one of those actions is occurring.

### Remediation
<a name="waf-7-remediation"></a>

For instructions on adding a rule to a rule group, see [Creating an AWS WAF Classic rule group](https://docs.aws.amazon.com/waf/latest/developerguide/classic-create-rule-group.html) in the *AWS WAF Developer Guide*.

## [WAF.8] AWS WAF Classic global web ACLs should have at least one rule or rule group
<a name="waf-8"></a>

**Related requirements:** NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(21)

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::WAF::WebACL`

**AWS Config rule:** [`waf-global-webacl-not-empty`](https://docs.aws.amazon.com/config/latest/developerguide/waf-global-webacl-not-empty)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF global web ACL contains at least one WAF rule or WAF rule group. The control fails if a web ACL does not contain any WAF rules or rule groups.

A WAF global web ACL can contain a collection of rules and rule groups that inspect and control web requests. If a web ACL is empty, the web traffic can pass without being detected or acted upon by WAF depending on the default action.

### Remediation
<a name="waf-8-remediation"></a>

To add rules or rule groups to an empty AWS WAF global web ACL, see [Editing a web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-editing.html) in the *AWS WAF Developer Guide*. For **Filter**, choose **Global (CloudFront)**.

## [WAF.10] AWS WAF web ACLs should have at least one rule or rule group
<a name="waf-10"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Protect > Secure network configuration

**Severity:** Medium

**Resource type:** `AWS::WAFv2::WebACL`

**AWS Config rule:** [`wafv2-webacl-not-empty`](https://docs.aws.amazon.com/config/latest/developerguide/wafv2-webacl-not-empty.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAFV2 web access control list (web ACL) contains at least one rule or rule group. The control fails if a web ACL does not contain any rules or rule groups.

A web ACL gives you fine-grained control over all of the HTTP(S) web requests that your protected resource responds to. A web ACL should contain a collection of rules and rule groups that inspect and control web requests. If a web ACL is empty, the web traffic can pass without being detected or acted upon by AWS WAF depending on the default action.

### Remediation
<a name="waf-10-remediation"></a>

To add rules or rule groups to an empty WAFV2 web ACL, see [Editing a Web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-editing.html) in the *AWS WAF Developer Guide*.

## [WAF.11] AWS WAF web ACL logging should be enabled
<a name="waf-11"></a>

**Related requirements:** NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Low

**Resource type:** `AWS::WAFv2::WebACL`

**AWS Config rule:** [`wafv2-logging-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/wafv2-logging-enabled.html) ``

**Schedule type:** Periodic

**Parameters:** None

This control checks whether logging is activated for an AWS WAFV2 web access control list (web ACL). This control fails if logging is deactivated for the web ACL.

**Note**  
This control doesn't check whether AWS WAF web ACL logging is enabled for an account through Amazon Security Lake.

Logging maintains the reliability, availability, and performance of AWS WAF. In addition, logging is a business and compliance requirement in many organizations. By logging traffic that's analyzed by your web ACL, you can troubleshoot application behavior.

### Remediation
<a name="waf-11-remediation"></a>

To activate logging for an AWS WAF web ACL, see [Managing logging for a web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/logging-management.html) in the *AWS WAF Developer Guide*.

## [WAF.12] AWS WAF rules should have CloudWatch metrics enabled
<a name="waf-12"></a>

**Related requirements:** NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-7(8), NIST.800-171.r2 3.14.6, NIST.800-171.r2 3.14.7

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::WAFv2::RuleGroup`

**AWS Config rule:** [`wafv2-rulegroup-logging-enabled`](https://docs.aws.amazon.com/config/latest/developerguide/wafv2-rulegroup-logging-enabled.html) ``

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an AWS WAF rule or rule group has Amazon CloudWatch metrics enabled. The control fails if the rule or rule group doesn't have CloudWatch metrics enabled.

Configuring CloudWatch metrics on AWS WAF rules and rule groups provides visibility into traffic flow. You can see which ACL rules are triggered and which requests are accepted and blocked. This visibility can help you identify malicious activity on your associated resources.

### Remediation
<a name="waf-12-remediation"></a>

To enable CloudWatch metrics on an AWS WAF rule group, invoke the [ UpdateRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_UpdateRuleGroup.html) API. To enable CloudWatch metrics on an AWS WAF rule, invoke the [ UpdateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_UpdateWebACL.html) API. Set the `CloudWatchMetricsEnabled` field to `true`. When you use the AWS WAF console to create rules or rule groups, CloudWatch metrics are automatically enabled.