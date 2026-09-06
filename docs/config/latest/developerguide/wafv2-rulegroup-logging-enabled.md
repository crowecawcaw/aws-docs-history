

# wafv2-rulegroup-logging-enabled
<a name="wafv2-rulegroup-logging-enabled"></a>

Checks if Amazon CloudWatch security metrics collection on AWS WAFv2 rule groups is enabled. The rule is NON\_COMPLIANT if the 'VisibilityConfig.CloudWatchMetricsEnabled' field is set to false. 

**Context**: AWS WAFV2 (Web Application Firewall version 2) allows you to create AWS WAF rules to protect your web applications from common web exploits and vulnerabilities. An AWS WAF rule group is a collection of AWS WAF rules that you can associate with a web ACL (Access Control List) to define the desired behavior for your web application traffic. For more information, see [AWS WAF rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html) and [Rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-groups.html) in the *AWS WAF Developer Guide*. 

By configuring CloudWatch security metrics collection on AWS WAFV2 rules group, you can monitor security metrics such as successful or failed Distributed denial of service (DDoS), SQL injection, and Cross-site scripting (XSS) attacks. The security metrics collected can help you simplify your investigations.

**Note**  
If there are no AWS WAF rules in the AWS WAFV2 rule group for the AWS Config managed rule to check, the AWS Config managed rule returns `NOT_APPLICABLE`.

**Identifier:** WAFV2\_RULEGROUP\_LOGGING\_ENABLED

**Resource Types:** AWS::WAFv2::RuleGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1617c23"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).