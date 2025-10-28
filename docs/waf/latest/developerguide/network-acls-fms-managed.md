**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using network ACL rules and tagging in Firewall Manager

This section describes the network ACL policy rule specifications and the network ACLs that are managed by Firewall Manager.

###### Tagging on a managed network ACL

Firewall Manager tags a managed network ACL with a `FMManaged` tag that has a value of `true`. Firewall Manager only
performs remediation on network ACLs that have this tag setting.

###### Rules that you define in the policy

In your network ACL policy specification, you define the rules that you want to run
first and last for inbound traffic and the rules that you want to run first and last for outbound traffic.

By default, you can define up to 5 inbound rules, for use in any combination of first and last rules
in the policy. Similarly, you can define up to 5 outbound rules.
For more about these limits, see
[Soft quotas](fms-limits.md#fms-limits-mutable "fms-limits.md#fms-limits-mutable").
For information about the general limits on network ACLs, see [Amazon VPC quotas on network ACLs](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-nacls "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-nacls") in the _Amazon VPC User Guide_.

You don't assign rule numbers to the policy rules. Instead, you specify
the rules in the order you want them to be evaluated, and Firewall Manager uses that ordering to assign rule numbers in the network ACLs that it manages.

Other than this, you manage the policy's network ACL rules specifications as you would manage the rules in a network ACL through Amazon VPC.
For information about network ACL management in Amazon VPC, see
[Control traffic to subnets
using network ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") and [Work with network
ACLs](../../../vpc/latest/userguide/vpc-network-acls.md#nacl-tasks "../../../vpc/latest/userguide/vpc-network-acls.md#nacl-tasks") in the **Amazon VPC User Guide**.

###### Rules in a managed network ACL

Firewall Manager configures the rules in a network ACL that it manages by placing the policy's first and last rules before and after any custom rules that an individual account manager defines. Firewall Manager preserves the order of the custom rules. Network ACLs are evaluated starting with the lowest numbered rule.

When Firewall Manager first creates a network ACL, it defines the rules with the following numbering:

- **First rules: 1, 2, ...** – Defined by you in the Firewall Manager network ACL policy.

Firewall Manager assigns rule numbers starting from 1 with increments of 1, with the rules ordered as you have ordered them in the policy specification.

- **Custom rules: 5,000, 5,100, ...** –
  Managed by individual account managers through Amazon VPC.

Firewall Manager assigns numbers to these rules
starting from 5,000 and incrementing by 100 for each subsequent rule.

- **Last rules: ... 32,765, 32,766** – Defined by you in the Firewall Manager network ACL policy.

Firewall Manager assigns rule numbers that end at the highest possible number, 32766 with increments of 1, with the rules ordered as you have ordered them in the policy specification.
After network ACL initialization, Firewall Manager doesn't control changes that individual accounts make in its managed network ACLs.
Individual accounts can change a network ACL without taking it out of compliance, providing any custom rules remain
numbered in between the policy's first and last rules, and the first and last rules maintain their specified ordering. As
a best practice, when managing custom rules, adhere to the numbering described in this section.
