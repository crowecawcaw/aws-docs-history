**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS WAF Distributed Denial of Service (DDoS) prevention

AWS WAF offers sophisticated and customizable protection against DDoS attacks in your AWS resources. Review the options described in this section and
select the level of Anti-DDoS protection that meets your security and business needs.

You can choose from two tiers of DDoS protection in AWS WAF:

Resource-level DDoS protection

The standard tier works within Application Load Balancers to defend against known malicious sources through on-host filtering.
You can configure the protective behavior to best react to potential DDoS events.

Resource-level DDoS protection:

- Monitors your traffic patterns automatically.
- Updates threat intelligence in real time.
- Protects against known malicious sources.

AWS managed rule group DDoS protection

The advanced tier of DDoS protections is offered through the `AWSManagedRulesAntiDDoSRuleSet`. The managed rule group complements the resource-level tier of protection,
with the following notable differences:

- Protection extends to both Application Load Balancers and CloudFront distributions
- Traffic baselines are created for your protected resources to improve detection of novel attack patterns.
- Protective behavior is activated according to sensitivity levels you select.
- Manages and labels requests to protected resources during probable DDoS events.

For a comprehensive list of the rules and functionality included, see [AWS WAF Distributed Denial of Service (DDoS) prevention rule group](aws-managed-rule-groups-anti-ddos.md "aws-managed-rule-groups-anti-ddos.md").

###### Note

You are charged additional fees when you use this managed rule group. For more information, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### Topics

- [Resource-level DDoS protection for Application Load Balancers](waf-anti-ddos-alb.md "waf-anti-ddos-alb.md")
- [Advanced Anti-DDoS protection using the AWS WAF Anti-DDoS managed rule group](waf-anti-ddos-advanced.md "waf-anti-ddos-advanced.md")
