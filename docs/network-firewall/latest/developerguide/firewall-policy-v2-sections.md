

# The firewall section and the IPS section
<a name="firewall-policy-v2-sections"></a>

A Next Generation policy is organized into two *sections*, one for each inspection engine. A section is a policy setting that holds the rules the engine evaluates:

Firewall section  
Holds the rules evaluated by the firewall engine, the access-control engine that is drop by default.

IPS section  
Holds the rules evaluated by the IPS engine, the intrusion detection and prevention engine that is pass by default.

The firewall section and the IPS section are both policy settings that you define when you create or update the policy. For the definitions of these two settings in the policy, see [Next Generation policy settings in AWS Network Firewall](firewall-policy-v2-settings.md). For more information about the two engines, see [The firewall engine and the IPS engine](firewall-policy-v2-engines.md).

**Adding rules to a section**  
Within either section, you can add rules in two ways, and you can combine both in the same section:
+ **Referenced rule groups** – References to rule groups that exist as separate, reusable resources. You can reuse a referenced rule group across multiple policies and share it across accounts. For information about creating rule groups, see [Working with firewall rule groups in AWS Network Firewall](firewall-rule-groups.md) and [Working with IPS rule groups in AWS Network Firewall](ips-rule-groups.md).
+ **Embedded rules** – Rules that you author directly in the policy, also called inline rules. Embedded rules are part of the policy and share its lifecycle. In the console, you add embedded rules by choosing **Add rule group**, then **Add embedded rules** when you add rule groups to a section. Unlike a referenced rule group, embedded rules don't require you to reserve capacity up front, but they can't be shared or reused across policies. For a full description of embedded rules, their capacity benefit, and their limitations, see [Embedded rules in a Next Generation policy](firewall-policy-v2-embedded-rules.md).

For the maximum number of rule groups that you can reference in each section, see [AWS Network Firewall quotas](quotas.md).

**Evaluation order**  
In the firewall section, each entry has a unique priority from 1–65535 that sets its evaluation order within the policy, with the lowest number evaluated first. In the IPS section, entries don't have a priority; the IPS engine evaluates its rules in the default action order (pass, then drop, then reject, then alert). The IPS engine in a Next Generation policy doesn't support strict rule evaluation order.