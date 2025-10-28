**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Advanced Anti-DDoS protection using the AWS WAF Anti-DDoS managed rule group

The `AWSManagedRulesAntiDDoSRuleSet` managed rule group is the most advanced tier of Anti-DDoS protections available in AWS WAF.

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

## AWS WAF Anti-DDoS protection components

The main components for implementing advanced Anti-DDoS protection in AWS WAF include the following:

**`AWSManagedRulesAntiDDoSRuleSet`** –
Detects, labels, and challenges requests that are likely participating
in a DDoS attack. It also labels all requests to a protected resource during an event.
For details about the rule group's rules and labels, see [AWS WAF Distributed Denial of Service (DDoS) prevention rule group](aws-managed-rule-groups-anti-ddos.md "aws-managed-rule-groups-anti-ddos.md"). To use this rule group,
include it in your protection pack (web ACL) using a managed rule group reference statement. For information,

see [Adding the Anti-DDoS managed rule group to your protection pack (web ACL)](waf-anti-ddos-rg-using.md "waf-anti-ddos-rg-using.md").

- **Web ACL traffic overview dashboards** – Provide monitoring
  for DDoS activity and anti-DDoS responses in the console. For more information,
  see [Traffic overview dashboards for protection packs (web ACLs)](web-acl-dashboards.md "web-acl-dashboards.md").
- **Logging and metrics** – Allow you to monitor traffic
  and understand Anti-DDoS protection effects. Configure logs, Amazon Security Lake data collection, and Amazon CloudWatch metrics
  for your protection pack (web ACL). For information about these options, see
  [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md"),
  [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"),
  and [What is Amazon Security Lake?](../../../security-lake/latest/userguide/what-is-security-lake.md "../../../security-lake/latest/userguide/what-is-security-lake.md").
- **Labels and label matching rules** – Allow you to customize
  handling of web requests identified by the Anti-DDoS managed rule group. For any rule
  in `AWSManagedRulesAntiDDoSRuleSet`, you can switch to count mode and match against added labels. For more
  information, see [Label match rule
  statement](waf-rule-statement-type-label-match.md "waf-rule-statement-type-label-match.md") and [Web request labeling in AWS WAF](waf-labels.md "waf-labels.md").
- **Custom requests and responses** – Allow you to add custom
  headers to allowed requests and send custom responses for blocked requests. Pair label matching
  with AWS WAF custom request and response features. For more information, see
  [Customized web requests and responses in
  AWS WAF](waf-custom-request-response.md "waf-custom-request-response.md").
