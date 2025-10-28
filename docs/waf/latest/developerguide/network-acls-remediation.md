**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# How Firewall Manager remediates noncompliant managed network ACLs

This section describes how Firewall Manager remediates its managed network ACLs when they're out of compliance with the policy. Firewall Manager
only remediates managed network ACLs—with the `FMManaged` tag set to `true`. For
network ACLs that aren't managed by Firewall Manager, see [Initial network ACL management](network-acls-initialization.md "network-acls-initialization.md").

Remediation restores the relative locations of the first, custom, and last rules and
restores the ordering for first and last rules.
During remediation, Firewall Manager won't necessarily move rules to the rule numbers that it uses in network ACL initialization.
For the initial number settings and descriptions of these rule categories, see [Initial network ACL management](network-acls-initialization.md "network-acls-initialization.md").

In order to establish compliant rules and rule ordering, Firewall Manager might need to move rules around inside the network ACL.
As much as possible, Firewall Manager preserves the network ACL's protections by maintaining existing compliant rule ordering as it does this.
For example, it might temporarily duplicate rules to new locations, and then
perform an ordered removal of the original rules, preserving relative locations during the process.

This approach protects your settings, but it also requires space
in the network ACL for the interim rules. If Firewall Manager hits the limit for
rules in a network ACL, it will halt remediation. When this happens,
the network ACL remains out of compliance and Firewall Manager reports the reason.

If an account adds custom rules to a network ACL that's managed by Firewall Manager, and those rules interfere with Firewall Manager remediation,
Firewall Manager stops any remediation activities on the network ACL and reports the conflict.

###### Forced remediation

If you choose auto remediation for the policy, you also specify whether to force remediation for the first rules or last rules.

When Firewall Manager encounters a conflict in traffic handling between a custom rule and a policy rule, it refers to the corresponding forced remediation setting. If forced remediation
is enabled, Firewall Manager applies the remediation, in spite of the conflict. If this option isn't enabled, Firewall Manager halts remediation. In either case, Firewall Manager reports
the rule conflict and offers remediation options.

###### Rule count requirements and limitations

During remediation, Firewall Manager might temporarily duplicate rules in order to move them without altering the protections that they provide.

For either inbound or outbound rules, the greatest number of rules that Firewall Manager might require to perform remediation is the following:

```
2 * (the number of rules defined in the policy for the traffic direction)
+
the number of custom rules defined in the network ACL for the traffic direction
```

Network ACLs and network ACL policies are bound by mutable rule limits. If Firewall Manager hits a limit in its
remediation efforts, it stops trying to remediate and reports the noncompliance.

To make room for Firewall Manager to perform its remediation activities, you might
request a limit increase. Alternately, you can change the configuration in the policy or network ACL to reduce the number of rules used.

For information about the network ACL limits, see [Amazon VPC quotas on network ACLs](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-nacls "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-nacls") in the _Amazon VPC User Guide_.

###### When remediation fails

While updating a network ACL, if Firewall Manager needs to stop for any reason, it
doesn't roll back the changes, but instead leaves the network ACL in an
interim state. If you see duplicate rules in a network ACL that has
the `FMManaged` tag set to `true`, Firewall Manager
is probably in the middle of remediating it. Changes might be partially complete for a period, but because of the
approach Firewall Manager takes to remediation, this won't
interrupt traffic or reduce the protection for associated subnets.

When Firewall Manager doesn't completely remediate network ACLs that are out of compliance, it reports the noncompliance for the associated subnets and suggests possible remediation options.

###### Retrying after remediation fails

In most cases, if Firewall Manager fails to complete remediation changes to a network ACL,
it will eventually retry the change.

The exception to this is when remediation reaches the network ACL rule count limit or the VPC network ACL count limit. Firewall Manager can't
perform remediation activities that take AWS resources over their limit settings.
In these cases, you need to reduce counts or increase limits in order to proceed. For information about the limits, see [Amazon VPC quotas on network ACLs](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-nacls "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-nacls") in the _Amazon VPC User Guide_.

## Firewall Manager network ACL compliance reporting

Firewall Manager monitors and reports compliance for all network ACLs that are attached to in-scope subnets.

Generally speaking, noncompliance occurs for situations such as incorrect rule ordering or a conflict in
traffic handling behavior between policy rules and custom rules. Noncompliance reporting includes
compliance violations and remediation options.

Firewall Manager reports compliance violations for a network ACL policy in the same way as for other policy types.
For information about compliance reporting, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md").

###### Noncompliance during policy updates

After you modify a network ACL policy, until Firewall Manager updates the network ACLs
that are in scope of the policy, Firewall Manager marks those network ACLs
noncompliant. Firewall Manager does this even if the network ACLs might, strictly speaking, be in compliance.

For example, if you remove rules from the policy specification, while
in-scope network ACLs still have the extra rules, their rule definitions
might still comply with the policy. However, since the extra rules are
part of the rules that Firewall Manager is managing, Firewall Manager views them as
violations of current policy settings. This is different from how
Firewall Manager views custom rules that you add to the Firewall Manager managed network ACLs.
