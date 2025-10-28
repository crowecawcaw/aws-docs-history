# Setting rule group capacity in AWS Network Firewall

AWS Network Firewall uses capacity settings to calculate and manage the processing requirements
for its rules groups and firewall policies. Each rule group must have a capacity setting
that's fixed at creation. When you reference a rule group from a firewall policy,
Network Firewall reserves the rule group's capacity in the policy, increasing the total
capacity that's used by the policy.

Using the **consumed capacity** fields in the console, you can also describe a rule group or a policy to find out
how much of the rule group or policy capacity is currently in use.

For information about the maximum capacity settings
for rule groups and firewall policies, see [AWS Network Firewall quotas](quotas.md "quotas.md").

You can't change or exceed a rule group's capacity when you make changes to it, so when you
set the rule group's capacity, leave room for it to grow.

###### Important

Network Firewall active threat defense managed rule groups have rule capacity limits that differ from the rule capacity limits that apply to other rule groups. For information,
see [AWS active threat defense for AWS Network Firewall](aws-managed-rule-groups-atd.md "aws-managed-rule-groups-atd.md")

## Stateless rule group capacity

Estimate a stateless rule group's capacity as the sum of the capacities of the rules that
you expect to have in it.

The capacity required for a single rule is the product of the complexity values of all of
its match settings.

- A match setting with no criteria specified has a complexity value of 1.
  Through the console, the **All** and **Any**
  settings are equivalent to providing no criteria, and they have a complexity
  value of 1.
- A match setting with criteria specifications has a complexity
  value equal to the number of specifications in the
  setting. For example, a protocol specification set
  to `UDP` and a source specification set
  to `10.0.0.0/24` each have a value of 1.
  A protocol set to `UDP`, `TCP`
  has a value of 2 and a source set to
  `10.0.0.0/24`,
  `10.0.1.0/24`, `10.0.2.0/24`
  has a value of 3.

The following lists example calculations of stateless rule capacity requirements.

- A rule with protocol that specifies the two settings
  `UDP`, `TCP` and source with
  the three settings `10.0.0.0/24`,
  `10.0.1.0/24`, `10.0.2.0/24`
  and single or no specifications for the other match
  settings has a capacity requirement of 6.
- A rule with a protocol that specifies 30 different protocols, a source with 3
  settings, and single or no specifications for the other match settings has a
  capacity requirement of 90.
- A rule with a protocol that specifies 30 different
  protocols, a source with 3 settings, a destination
  with 5 settings, and single or no specifications for
  the other match settings has a capacity requirement
  of (30\*3\*5) = 450.

To calculate the capacity of a rule group, add the capacity requirements of all rules that
you expect to have in the rule group during its lifetime. You can't change this
setting after you create the rule group.

The maximum capacity setting for a stateless rule group is
30,000.

## Stateful rule group capacity

Estimate a stateful rule group's capacity as the number of rules that you expect to have in
it during its lifetime. You can't change this setting after you create the rule
group.

The maximum capacity setting for a stateful rule group is
50,000.
