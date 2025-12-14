**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using content audit security group policies with Firewall Manager

This page explains how Firewall Manager content audit security group policies work.

Use AWS Firewall Manager content audit security group policies to audit and apply policy actions to the rules that are
in use in your organization's security groups. Content audit security group policies
apply to all customer-created security groups in use in your AWS organization,
according to the scope that you define in the policy.

For guidance on
creating a content audit security group policy using the console, see [Creating a
content audit security group policy](create-policy.md#creating-firewall-manager-policy-audit-security-group "create-policy.md#creating-firewall-manager-policy-audit-security-group").

###### Policy scope resource type

You can apply content audit security group policies to the following resource
types:

- Amazon Elastic Compute Cloud (Amazon EC2) instance
- Elastic Network Interface
- Amazon VPC security group
  Security groups are considered in scope of the policy if they explicitly are in
  scope or if they're associated with resources that are in scope.

###### Policy rule options

You can use either managed policy rules or custom policy rules for each
content audit policy, but not both.

- **Managed policy rules** – In a policy with managed
  rules, you can use application and protocol lists to control which rules that Firewall Manager audits and either marks as compliant or non-compliant. You can use lists that are managed by Firewall Manager. You can also create and use your own application and protocol lists.
  For information about these types of lists and your management options for
  custom lists, see [Using Firewall Manager managed lists](working-with-managed-lists.md "working-with-managed-lists.md").
- **Custom policy rules** – In a policy
  with custom policy rules, you specify an existing security group as the
  audit security group for your policy. You can use the audit security group
  rules as a template that defines the rules that Firewall Manager audits and either marks as compliant or non-compliant.

###### Audit security groups

You must create audit
security groups using your Firewall Manager administrator account, before you can use them in
your policy. You can manage security groups through Amazon Virtual Private Cloud (Amazon VPC) or Amazon Elastic Compute Cloud
(Amazon EC2). For information, see [Working
with Security Groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md#WorkingWithSecurityGroups "../../../vpc/latest/userguide/VPC_SecurityGroups.md#WorkingWithSecurityGroups") in the _Amazon VPC User Guide_.

A security group that you use for a content audit security group policy is
used by Firewall Manager only as a comparison reference for the security groups that are in
scope of the policy. Firewall Manager doesn't associate it with any resources in your
organization.

The way that you define the rules in the audit security group depends on your
choices in the policy rules settings:

- **Managed policy rules** – For managed policy rules
  settings, you use an audit security group to override other settings in the
  policy, to explicitly allow or deny rules that otherwise might have another
  compliance outcome.
  - If you choose to always _allow_ the rules that are defined in the
    audit security group, any rule that matches one that's defined in
    the audit security group is considered
    _compliant_ with the policy, regardless of
    the other policy settings.
  - If you choose to always _deny_ the rules that are defined in the
    audit security group, any rule that matches one that's defined in
    the audit security group is considered
    _noncompliant_ with the policy, regardless of
    the other policy settings.

- **Custom policy rules** – For custom
  policy rules settings, the audit
  security group provides the example of what is acceptable or not acceptable in
  the in-scope security group rules:
  - If you choose to _allow_ the use of the rules, all in-scope security
    groups must only have rules that are _within_ the
    allowed range of the policy's audit security group rules.
    _In this case, the policy's security group rules
    provide the example of what's acceptable to
    do._
  - If you choose to _deny_ the use of the rules, all in-scope security
    groups must only have rules that are _not within_
    the allowed range of the policy's audit security group rules.
    _In this case, the policy's security group provides the
    example of what's not acceptable to do._

###### Policy creation and management

When you create an audit security group policy, you must have automatic
remediation disabled. The recommended practice is to review the effects of
policy creation before enabling automatic remediation. After you review the
expected effects, you can edit the policy and enable automatic remediation. When
automatic remediation is enabled, Firewall Manager updates or removes rules that are
noncompliant in in-scope security groups.

###### Security groups affected by an audit security group policy

All security groups in your organization that are customer-created are
eligible to be in scope of an audit security group policy.

Replica security groups are not customer-created and so aren't eligible to be
directly in scope of an audit security group policy. However, they can be updated as
a result of the policy's automatic remediation activities. A common security group
policy's primary security group is customer-created and can be in scope of an audit
security group policy. If an audit security group policy makes changes to a primary
security group, Firewall Manager automatically propagates those changes to the replicas.

## Caveats and limitations for content audit security group policies

You cannot reference peer security groups in a content audit security group policy.

For information on other considerations across all Firewall Manager security groups, see [Security group policy caveats and
limitations](security-group-policies.md#security-groups-limitations "security-group-policies.md#security-groups-limitations").
