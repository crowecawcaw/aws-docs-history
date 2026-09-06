

# AWS active threat defense for AWS Network Firewall
<a name="aws-managed-rule-groups-atd"></a>

 The active threat defense managed rule group provides advanced network threat protection for your Network Firewall firewall policies. AWS continuously updates these rules based on Amazon threat intelligence to protect against active threats and cloud-specific attack patterns. While complementing existing AWS managed rule groups, active threat defense specifically uses Amazon threat intelligence from MadPot, an internal AWS threat intelligence and disruption service. For more information about MadPot, see [ Meet MadPot, a threat intelligence tool Amazon uses to protect customers from cybercrime](https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime). 

AWS Network Firewall currently supports the `AttackInfrastructure` active threat defense rule group.

Each rule group name in the table below is appended by either `StrictOrder` or `ActionOrder`. A firewall policy's *rule evaluation order* determines whether you can add `StrictOrder` or `ActionOrder` managed rule groups to the policy. For example, you can only add a rule group appended with `StrictOrder` if the policy uses strict order for its rule evaluation order. 

**Note**  
In the console, Network Firewall automatically filters the managed rule groups available for you to add to your policy. For information about rule evaluation order, see [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md).


| Rule group name | Maximum rule capacity per rule group | Description | 
| --- | --- | --- | 
| `AttackInfrastructureStrictOrder`,<br />`AttackInfrastructureActionOrder` | 15,000 | Protects against threat activity by blocking communication with known harmful infrastructure tracked by AWS. This includes:+ Malware staging URLs<br />+ Botnet command and control servers<br />+ Crypto-mining pools<br />Implements comprehensive filtering of both inbound and outbound traffic for multiple protocols, including TCP, TLS, HTTP, and outbound UDP.<br />Uses verified threat indicators to ensure high accuracy and minimize false positives. AWS automatically removes threat indicators when there is no evidence of related threat activity. | 

**Important**  
Network Firewall active threat defense managed rule groups have rule capacity limits that differ from the rule capacity limits that apply to other rule groups.

## Get started with active threat defense
<a name="atd-next-steps"></a>

To start using the active threat defense, complete the following tasks:

1. Add the `AttackInfrastructure` rule group to your firewall policy. For instructions, see [Working with AWS managed rule groups in the Network Firewall console](nwfw-using-managed-rule-groups-console.md).
**Tip**  
After you add the rule group to your policy, you don't need to take any action to receive updates. AWS automatically updates the rules based on the latest threat intelligence.

1. Configure your firewall policy to use either strict order or action order evaluation. This determines which version of the rule group you can add. For more information, see [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md).

1. Optionally monitor your firewall's activity using CloudWatch Logs. For information about monitoring Network Firewall, see [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md).

To learn more about active threat defense managed rule groups, review the topics in this guide:

**Topics**
+ [Get started with active threat defense](#atd-next-steps)
+ [Understanding active threat defense managed rule group indicators](atd-indicators.md)
+ [Deep threat inspection for active threat defense managed rule groups](atd-deep-threat-inspection.md)