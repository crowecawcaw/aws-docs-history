

# Setting rule group capacity in AWS Network Firewall

AWS Network Firewall uses capacity settings to calculate and manage the processing requirements for its rule groups and firewall policies. Each rule group must have a capacity setting that's fixed at creation. When you reference a rule group from a firewall policy, Network Firewall reserves the rule group's capacity in the policy, increasing the total capacity that's used by the policy.

Using the **consumed capacity** fields in the console, you can also describe a rule group or a policy to find out how much of the rule group or policy capacity is currently in use.

For information about the maximum capacity settings for rule groups and firewall policies, see [AWS Network Firewall quotas](quotas.md).

You can't change or exceed a rule group's capacity when you make changes to it, so when you set the rule group's capacity, leave room for it to grow.

In a Next Generation policy, the firewall engine and the IPS engine have *dedicated, separate* rule capacity: 30,000 rules for the firewall engine and 50,000 rules for the IPS engine, for a combined total of 80,000 rules per policy. Because the two pools are separate, the rules in one engine never reduce the capacity available to the other. This differs from a Classic Network Firewall policy, where all stateful rules share a single pool with a default capacity of 30,000 and an adjustable maximum of 50,000 rules per policy.

Embedded rule groups—the rules that you author directly in a policy's firewall or IPS section rather than in a separate, referenced rule group—use variable capacity. They don't reserve a fixed capacity up front; instead, they draw from the engine's remaining capacity after the policy accounts for the fixed capacity reserved by the referenced (shared) rule groups in that engine's section. For a full description of embedded rules and how to add them to a policy section, see [Embedded rules in a Next Generation policy](firewall-policy-v2-embedded-rules.md).