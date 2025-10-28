**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using common security group

policies with Firewall Manager

This page explains how Firewall Manager common security group policies work.

With a common security group policy, Firewall Manager provides a centrally controlled association of
security groups to accounts and resources across your organization. You specify
where and how to apply the policy in your organization.

You can apply common security group policies to the following resource types:

- Amazon Elastic Compute Cloud (Amazon EC2) instance
- Elastic Network Interface
- Application Load Balancer
- Classic Load Balancer
  For guidance on
  creating a common security group policy using the console, see [Creating a
  common security group policy](create-policy.md#creating-firewall-manager-policy-common-security-group "create-policy.md#creating-firewall-manager-policy-common-security-group").

###### Shared VPCs

In the policy scope settings for a common security group policy, you can choose to include
shared VPCs. This choice includes VPCs that are owned by another account and
shared with an in-scope account. VPCs that in-scope accounts own are always
included. For information about shared VPCs, see [Working with shared VPCs](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the
_Amazon VPC User Guide_.

The following caveats apply to including shared VPCs. These are in addition to the general caveats for security group policies at [Security group policy caveats and
limitations](security-group-policies.md#security-groups-limitations "security-group-policies.md#security-groups-limitations").

- Firewall Manager replicates the primary security group into the VPCs for each in-scope account. For
  a shared VPC, Firewall Manager replicates the primary security group once for each
  in-scope account that the VPC is shared with. This can result in multiple
  replicas in a single shared VPC.
- When you create a new shared VPC, you won’t see it represented in the
  Firewall Manager security group policy details until after you create at least one
  resource in the VPC that's within the scope of the policy.
- When you disable shared VPCs in a policy that had shared VPCs enabled, in
  the shared VPCs, Firewall Manager deletes the replica security groups that aren’t
  associated with any resources. Firewall Manager leaves the remaining replica security
  groups in place, but stops managing them. Removal of these remaining
  security groups requires manual management in each shared VPC
  instance.

###### Primary security groups

For each common security group policy, you provide AWS Firewall Manager with one or more
primary security groups:

- Primary security groups must be created by the Firewall Manager administrator account
  and can reside in any Amazon VPC instance in the account.
- You manage your primary security groups through Amazon Virtual Private Cloud (Amazon VPC) or
  Amazon Elastic Compute Cloud (Amazon EC2). For information, see [Working with Security Groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md#WorkingWithSecurityGroups "../../../vpc/latest/userguide/VPC_SecurityGroups.md#WorkingWithSecurityGroups") in the _Amazon VPC User Guide_.
- You can name one or more security groups as primaries for a Firewall Manager security
  group policy. By default, the number of security groups allowed in a policy
  is one, but you can submit a request to increase it. For information, see
  [AWS Firewall Manager quotas](fms-limits.md "fms-limits.md").

###### Policy rules settings

You can choose one or more of the following change control behaviors for the
security groups and resources of your common security group policy:

- Identify and report on any changes made by local users to replica security
  groups.
- Disassociate any other security groups from the AWS resources that are
  within the policy scope.
- Distribute tags from the primary group to the replica security groups.

###### Important

Firewall Manager won't distribute system tags added by AWS services into the replica security groups. System tags begin with the `aws:` prefix. Additionally, Firewall Manager won't update the tags of existing security groups or create new security groups if the policy has tags that conflict with the organization's tag policy. For information about tag policies, see [Tag policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md") in the AWS Organizations User Guide.

- Distribute security group references from the primary group to the replica security groups.

This enables you to easily establish common security group referencing rules across all in-scope resources to instances associated with the specified security group's VPC. When you enable this option, Firewall Manager only propagates the security group references if the security groups reference peer security groups in Amazon Virtual Private Cloud. If the replica security groups don't correctly reference the peer security group, Firewall Manager marks these replicated security groups as non-compliant. For information about how to reference peer security groups in Amazon VPC, see [Update your security groups to reference peer security groups](../../../vpc/latest/peering/vpc-peering-security-groups.md "../../../vpc/latest/peering/vpc-peering-security-groups.md") in the [Amazon VPC Peering Guide](../../../vpc/latest/peering.md "../../../vpc/latest/peering.md").

If you don't enable this option, Firewall Manager doesn't propagate security group references to the replica security groups. For information about VPC peering in Amazon VPC, see the [Amazon VPC Peering Guide](../../../vpc/latest/peering.md "../../../vpc/latest/peering.md").

###### Policy creation and management

When you create your common security group policy, Firewall Manager replicates the
primary security groups to every Amazon VPC instance within the policy scope, and
associates the replicated security groups to accounts and resources that are in
scope of the policy. When you modify a primary security group, Firewall Manager propagates
the change to the replicas.

When you delete a common security group policy, you can choose whether to clean up
the resources created by the policy. For Firewall Manager common security groups, these
resources are the replica security groups. Choose the cleanup option unless you want
to manually manage each individual replica after the policy is deleted. For most
situations, choosing the cleanup option is the simplest approach.

###### How replicas are managed

The replica security groups in the Amazon VPC instances are managed like other
Amazon VPC security groups. For information, see [Security Groups for Your
VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the _Amazon VPC User Guide_.
