

# Rule groups for Next Generation policies in AWS Network Firewall
<a name="rule-groups-v2"></a>

Next Generation policies use two rule group types, one for each inspection engine: *firewall rule groups* for the firewall engine and *IPS rule groups* for the IPS engine. These rule group types use the same `RuleGroup` resource and the same API operations as the stateless and stateful rule groups described in [Managing your rule groups](rule-groups.md)—`CreateRuleGroup`, `UpdateRuleGroup`, `DescribeRuleGroup`, `DeleteRuleGroup`, and `ListRuleGroups`. You select the rule group type when you create the rule group, and you can't change it afterward.

As with stateless and stateful rule groups, you can share firewall and IPS rule groups across accounts using AWS Resource Access Manager, and you can reference the same rule group from multiple policies. For information about sharing, see [Sharing Network Firewall resources](sharing.md). For the maximum number of rules per policy and other quotas, see [AWS Network Firewall quotas](quotas.md).

**Topics**
+ [Common rule group settings in AWS Network Firewall](rule-group-settings-v2.md)
+ [Viewing your rule groups in AWS Network Firewall](rule-groups-v2-viewing.md)
+ [Creating a rule group for a Next Generation policy](rule-groups-v2-creating.md)
+ [Updating a rule group for a Next Generation policy](rule-groups-v2-updating.md)
+ [Deleting a rule group for a Next Generation policy](rule-groups-v2-deleting.md)
+ [Working with firewall rule groups in AWS Network Firewall](firewall-rule-groups.md)
+ [Working with IPS rule groups in AWS Network Firewall](ips-rule-groups.md)
+ [Setting rule group capacity in AWS Network Firewall](rule-group-capacity-v2.md)