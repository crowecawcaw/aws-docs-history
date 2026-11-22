

# AWS active threat defense for AWS Network Firewall

 The active threat defense managed rule group provides advanced network threat protection for your Network Firewall firewall policies. AWS continuously updates these rules based on Amazon threat intelligence to protect against active threats and cloud-specific attack patterns. While complementing existing AWS managed rule groups, active threat defense specifically uses Amazon threat intelligence from MadPot, an internal AWS threat intelligence and disruption service. For more information about MadPot, see [ Meet MadPot, a threat intelligence tool Amazon uses to protect customers from cybercrime](https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime). 

AWS Network Firewall currently supports the `AttackInfrastructure` active threat defense rule group.

Each rule group name in the table below is appended by either `StrictOrder` or `ActionOrder`. A firewall policy's *rule evaluation order* determines whether you can add `StrictOrder` or `ActionOrder` managed rule groups to the policy. For example, you can only add a rule group appended with `StrictOrder` if the policy uses strict order for its rule evaluation order. 

This choice applies to Classic Network Firewall policies, whose rule evaluation order is strict order or action order. In a Next Generation policy, the AWS managed rule groups are IPS-typed copies of the Classic managed rule groups. They have the same names and rules but a different Amazon Resource Name (ARN) type. You reference them in the policy's *IPS engine* section, where the IPS engine evaluates them using action order, so you add the `ActionOrder` variant. For more information, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md) and [Working with IPS rule groups in AWS Network Firewall](ips-rule-groups.md).

**Note**  
When you reference a managed rule group through the API or AWS CLI (for example, in an `IpsRuleGroupEntry` for a Next Generation policy), use the IPS-typed ARN, which has the form `arn:aws:network-firewall:{{region}}:aws-managed:ips-rulegroup/{{Name}}`. This differs from the Classic managed rule group ARN, which has the form `arn:aws:network-firewall:{{region}}:aws-managed:stateful-rulegroup/{{Name}}`.

**Note**  
In the console, Network Firewall automatically filters the managed rule groups available for you to add to your policy. For information about rule evaluation order, see [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md).


| Rule group name | Maximum rule capacity per rule group | Description | 
| --- | --- | --- | 
| `AttackInfrastructureStrictOrder`,<br />`AttackInfrastructureActionOrder` | 15,000 | Protects against threat activity by blocking communication with known harmful infrastructure tracked by AWS. This includes:+ Malware staging URLs<br />+ Botnet command and control servers<br />+ Crypto-mining pools<br />Implements comprehensive filtering of both inbound and outbound traffic for multiple protocols, including TCP, TLS, HTTP, and outbound UDP.<br />Uses verified threat indicators to ensure high accuracy and minimize false positives. AWS automatically removes threat indicators when there is no evidence of related threat activity. | 

**Important**  
Network Firewall active threat defense managed rule groups have rule capacity limits that differ from the rule capacity limits that apply to other rule groups.

## Getting started with active threat defense
<a name="atd-next-steps"></a>

To start using the active threat defense, complete the following tasks:

1. Add the `AttackInfrastructure` rule group to your firewall policy. For instructions, see [Working with AWS managed rule groups in the Network Firewall console](nwfw-using-managed-rule-groups-console.md).
**Tip**  
After you add the rule group to your policy, you don't need to take any action to receive updates. AWS automatically updates the rules based on the latest threat intelligence.

1. Add the rule group variant that matches your policy type. In a *Classic Network Firewall* policy, set the policy's rule evaluation order and add the matching `StrictOrder` or `ActionOrder` rule group. In a *Next Generation* policy, the active threat defense managed rule group is an IPS-typed managed rule group that you reference in the policy's IPS engine section, where the IPS engine evaluates it using action order, so add the `ActionOrder` variant. In the console, choosing **Enable Active Threat Defense** adds this rule group for you. Through the API or AWS CLI, reference it using the IPS-typed ARN `arn:aws:network-firewall:{{region}}:aws-managed:ips-rulegroup/AttackInfrastructureActionOrder`. For more information, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md) and [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md).

1. Optionally monitor your firewall's activity using CloudWatch Logs. For information about monitoring Network Firewall, see [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md).

To learn more about active threat defense managed rule groups, review the topics in this guide:

**Topics**
+ [Getting started with active threat defense](#atd-next-steps)
+ [Understanding active threat defense managed rule group indicators](atd-indicators.md)
+ [Deep threat inspection for active threat defense managed rule groups](atd-deep-threat-inspection.md)