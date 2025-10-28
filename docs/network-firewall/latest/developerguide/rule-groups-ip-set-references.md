# IP set references in Suricata compatible AWS Network Firewall rule groups

You can use an IP set reference with **Suricata compatible rule strings** and with **standard Network Firewall stateful rule groups**.

An _IP set reference_ is a Network Firewall rule group
variable that references a set of IP addresses or CIDR
blocks contained in an AWS resource, such as an Amazon Virtual Private Cloud
prefix list. IP set references enable you to dynamically use
IP addresses or CIDRs from another AWS service in your
Suricata compatible rules. When you create, update, or
delete the IP sets that you reference in your rules,
Network Firewall automatically updates the rules with the
changes. For example, if you add five CIDRs to an IP set
resource that you're referencing in a rule, then the rule
will automatically include the five CIDRs that you added to
the resource.

Network Firewall currently supports the following AWS resources as IP set references:

- **Amazon VPC prefix lists**. For information about referencing Amazon VPC prefix lists in your rule groups, see the following section [Referencing Amazon VPC prefix lists](#rule-groups-referencing-prefix-lists "#rule-groups-referencing-prefix-lists").
- **Resource groups**. For information about referencing resource groups in your rule groups, see following section [Referencing resource groups](#rule-groups-referencing-resource-groups "#rule-groups-referencing-resource-groups").
  For an example of a rule that uses an IP set reference, see [Stateful rules examples: IP set reference](suricata-examples.md#suricata-example-rule-with-ip-set-reference "suricata-examples.md#suricata-example-rule-with-ip-set-reference").

For more information about adding IP sets to your Suricata compatible rule groups via the console, see the [Creating a stateful rule group](rule-group-stateful-creating.md "rule-group-stateful-creating.md") procedure.

## Limits for IP set references

The following limits apply to IP set references:

- Maximum of five IP set references per rule group. You can use IP set references in addition to
  IP set variables or port variables in a rule
  group. Only IP set references count against this
  limit.
- Maximum of 1,000,000 CIDRs - You can use a maximum of 1,000,000 CIDRs in all of the IP set references used in a single firewall. If you exceed this limit, then Network Firewall includes only the first 1,000,000 CIDRs from your referenced IP set resources. Network Firewall calculates CIDRs differently for prefix lists and resource groups:
  - Prefix lists – Network Firewall takes an aggregated account of the CIDRs in each referenced IP set.
  - Resource groups – Network Firewall calculates the number of IP addresses associated with all of the resources in the group, such as all of the IP addresses associated with an Amazon EC2 instance, both public and private.

## Referencing Amazon VPC prefix lists

A _prefix list_ is a set of one or more CIDR block entries that you can use to configure security groups, routing tables, and transit gateways in Amazon VPC. A reference to a prefix list helps you to simplify the management of the CIDR blocks in your rules. If you frequently use the same CIDRs across multiple rules, you can manage those CIDRs in a single prefix list, instead of repeatedly referencing the same CIDRs in each rule. If you need to remove a CIDR block, you can remove its entry from the prefix list instead of removing the CIDR from every affected rule.

For more information about Amazon VPC prefix lists, see [Group CIDR blocks using managed prefix lists](../../../vpc/latest/userguide/managed-prefix-lists.md "../../../vpc/latest/userguide/managed-prefix-lists.md") in the _Amazon VPC User Guide_.

## Referencing resource groups

A _tag-based resource group_ is a collection of AWS resources whose membership in a resource group is based on tags. Tags are key value metadata that you associated with a resource type, such as an Amazon EC2 instance. Similar to prefix lists, a reference to a resource group helps you to simplify the management of the IP addresses in your rules. If you frequently want to reference the IP addresses of the same set of resources, you can manage those IPs in a single resource group, instead of repeatedly referencing the same IPs in each rule. Network Firewall constantly checks for resources that match the resource group grouping criteria in your account, and then resolves IPs of the matching resources in the rule. If you need to remove a set of IP addresses, you can remove the tagged resource type from the resources group instead of removing the IP from every affected rule.

For more information about using resource groups in Network Firewall, see [Using tag-based resource groups in Network Firewall](resource-groups.md "resource-groups.md").
