**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using Amazon VPC network access control list (ACL) policies with Firewall Manager

This section covers how AWS Firewall Manager network ACL policies work and provides guidance for using them. For
guidance creating a network ACL policy using the console, see [Creating a
network ACL policy](create-policy.md#creating-firewall-manager-policy-network-acl "create-policy.md#creating-firewall-manager-policy-network-acl").

For information about Amazon VPC network access control lists (ACLs), see [Control traffic to subnets using network
ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") in the _Amazon VPC User Guide_.

You can use Firewall Manager network ACL policies to manage Amazon Virtual Private Cloud (Amazon VPC) network access control
lists (ACLs) for your organization in AWS Organizations. You define the policy's network ACL rule settings
and the accounts and subnets where you want the settings enforced.
Firewall Manager continuously applies your policy settings to accounts and subnets as
they are added or updated across your organization. For information about policy scope
and AWS Organizations, see [Using the AWS Firewall Manager policy scope](policy-scope.md "policy-scope.md") and the [AWS Organizations User Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md").

When you define a Firewall Manager network ACL policy, in addition to the standard Firewall Manager policy settings, such as name and scope,
you provide the following:

- First and last rules for inbound and outbound traffic handling. Firewall Manager enforces the presence and ordering of these in the network ACLs
  that are in scope of the policy, or reports noncompliance. Your individual accounts can create custom rules to run in between
  the policy's first and last rules.
- Whether to force remediation when remediation would result in traffic management conflicts between the rules in the network ACL. This
  applies only when remediation is enabled for the policy.

## Best practices for using Firewall Manager network ACL policies

This section lists recommendations for working with Firewall Manager network ACL policies and managed network ACLs.

###### Refer to the `FMManaged` tag to identify network ACLs that are managed by Firewall Manager

The network ACLs that Firewall Manager manages have the `FMManaged` tag set to
`true`. Use this tag to help distinguish your own custom network ACLs
from those that you're managing through Firewall Manager.

###### Don't modify the value of the `FMManaged` tag on a network ACL

Firewall Manager uses this tag to set and determine its management status with a network ACL.

###### Don't modify the associations for subnets that have Firewall Manager managed network ACLs

Don't manually change the associations between your subnets and
any network ACLs that are managed by Firewall Manager. Doing so can disable the ability of Firewall Manager to
manage protections for those subnets. You can identify network ACLs that are managed by Firewall Manager by looking
for the `FMManaged` tag settings of `true`.

To remove a subnet from Firewall Manager policy management, use the Firewall Manager policy scope settings
to exclude the subnet. For example, you can tag the subnet
and then exclude that tag from policy scope. For more information, see
[Using the AWS Firewall Manager policy scope](policy-scope.md "policy-scope.md").

###### When you update a managed network ACL, don't modify the rules that are managed by Firewall Manager

In a network ACL that's managed by Firewall Manager, keep your custom rules separated from
the policy rules by adhering to the numbering scheme described in
[Using network ACL rules and tagging in Firewall Manager](network-acls-fms-managed.md "network-acls-fms-managed.md").
Only add or modify rules that have numbers between 5,000 and 32,000.

###### Avoid adding too many rules for your account limits

During remediation of a network ACL, Firewall Manager usually increases the network ACL rule count temporarily.
To avoid noncompliance problems, make sure you have enough room for the rules you're using. For
more information, see [How Firewall Manager remediates noncompliant managed network ACLs](network-acls-remediation.md "network-acls-remediation.md").

###### Start with automatic remediation disabled

Start with automatic remediation disabled, and then review the policy details information to determine the
effects that automatic remediation would have. When you are satisfied that the
changes are what you want, edit the policy to enable automatic remediation.

## Firewall Manager network ACL policy caveats

This section lists the caveats and limitations for using Firewall Manager network ACL policies.

- **Slower update times than with other policies** –
  Firewall Manager generally applies network ACL policies and policy changes more
  slowly than with other Firewall Manager policies, due to limitations in
  the rate at
  which the Amazon EC2 network ACL APIs are able to process requests.
  You might notice that policy changes take longer than similar
  changes with other Firewall Manager policies, in particular when you first add
  a policy.
- **For initial subnet protection, Firewall Manager prefers older policies** – This applies only to
  subnets that aren't yet protected by a Firewall Manager network ACL policy. If a subnet comes into scope of more than one network ACL policy at the same time,
  then Firewall Manager uses the oldest policy to protect the subnet.
- **Reasons for a policy to stop protecting a subnet** – A policy that's managing the network ACL for a subnet retains management until one of the following happens:
  - The subnet goes out of scope of the policy.
  - The policy is deleted.
  - You manually change the subnet's association to a network ACL
    that's managed by a different Firewall Manager policy and for which the
    subnet is in scope.

###### Topics

- [Using network ACL rules and tagging in Firewall Manager](network-acls-fms-managed.md "network-acls-fms-managed.md")
- [How Firewall Manager initiates network ACL management for a subnet](network-acls-initialization.md "network-acls-initialization.md")
- [How Firewall Manager remediates noncompliant managed network ACLs](network-acls-remediation.md "network-acls-remediation.md")
- [Deleting a Firewall Manager network ACL policy](network-acls-deletion.md "network-acls-deletion.md")
