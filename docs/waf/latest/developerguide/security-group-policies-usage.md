**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using usage audit security group policies with Firewall Manager

This page explains how Firewall Manager usage audit security group policies work.

Use AWS Firewall Manager usage audit security group policies to monitor your organization for
unused and redundant security groups and optionally perform cleanup. When you enable
automatic remediation for this policy, Firewall Manager does the following:

1. Consolidates redundant security groups, if you've chosen that option.
2. Removes unused security groups, if you've chosen that option.
   You can apply usage audit security group policies to the following resource type:

- Amazon VPC security group
  For guidance on
  creating a usage audit security group policy using the console, see [Creating a
  usage audit security group policy](create-policy.md#creating-firewall-manager-policy-usage-security-group "create-policy.md#creating-firewall-manager-policy-usage-security-group").

###### How Firewall Manager detects and remediates redundant security groups

For security groups to be considered redundant, they must have exactly the same rules set
and be in the same Amazon VPC instance.

To remediate a redundant security group set,
Firewall Manager selects one of the security groups in the set to keep, and then associates
it to all resources that are associated with the other security groups in the
set. Firewall Manager then disassociates the other security groups from the resources they
were associated with, which renders them unused.

###### Note

If you have also chosen to remove unused security groups, Firewall Manager does that next. This can
result in the removal of the security groups that are in the redundant
set.

###### How Firewall Manager detects and remediates unused security groups

Firewall Manager considers a security group to be unused if both of the following are true:

- The security group is not used by any Amazon EC2 instance or Amazon EC2 elastic network interface.
- Firewall Manager hasn't received a configuration item for it within the number of minutes specified in the policy rule time period.
  The policy rule time period has a default setting of zero minutes, but you can increase the time up to 365 days (525,600 minutes), to
  give yourself time to associate new security groups with resources.

###### Important

If you specify a number of minutes other than the default value of zero,
you must enable indirect relationships in AWS Config. Otherwise, your usage audit
security group policies will not work as intended. For information about indirect
relationships in AWS Config, see [Indirect Relationships in
AWS Config](../../../config/latest/developerguide/faq.md#faq-2 "../../../config/latest/developerguide/faq.md#faq-2") in the _AWS Config Developer Guide_.

Firewall Manager remediates unused security groups by deleting them from your account according to your rules settings, if possible.
If Firewall Manager is unable to delete a security group, it marks it as noncompliant with the policy.
Firewall Manager can't delete a security group that's referenced by another security group.

The timing of the remediation varies according to whether you use the default time period setting or a custom setting:

- **Time period set to zero, the default** – With this setting, a
  security group is considered unused as soon as it's not being used by an Amazon EC2 instance or elastic network interface.

For this zero time period setting, Firewall Manager remediates the security group immediately.

- **Time period greater than zero** – With this setting, a security group
  is considered unused when it's not being used by an Amazon EC2 instance or elastic network interface and Firewall Manager hasn't received
  a configuration item for it within the specified number of minutes.

For the non-zero time period setting, Firewall Manager remediates the security group after it's remained in the unused state for 24 hours.

###### Default account specification

When you create a usage audit security group policy through the console, Firewall Manager
automatically chooses **Exclude the specified accounts and include all
others**. The service then puts the Firewall Manager administrator account in
the list to exclude. This is the recommended approach, and allows you to
manually manage the security groups that belong to the Firewall Manager administrator
account.
