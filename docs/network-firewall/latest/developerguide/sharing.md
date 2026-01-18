# Sharing AWS Network Firewall resources

You can share Network Firewall firewalls, firewall policies, and rule groups with other AWS accounts. When you share a firewall, other accounts can use your firewall's protections in their VPCs through VPC endpoint associations.
When you share firewall policies or rule groups, other accounts can use these resources in their own firewalls.

The owner of a firewall, firewall policy, or rule group can share a resource with:

- Specific AWS accounts inside or outside of its organization in AWS Organizations
- An organizational unit inside its organization in AWS Organizations
- Its entire organization in AWS Organizations

###### Considerations

Consideration the following when sharing AWS Network Firewall resources:

- Sharing a firewall enables other AWS accounts to create VPC endpoint associations in their VPCs. Each VPC endpoint association creates a new firewall endpoint that processes traffic according to the shared firewall's policy.
- You can't share a firewall policy that's configured to use [TLS inspection](tls-inspection-configurations.md "tls-inspection-configurations.md"). TLS inspection only works with primary VPC endpoints and same-account secondary endpoints.
- The owner of a rule group can share a rule group that refers to a [resource group](resource-groups.md "resource-groups.md"), but can't share the resource group itself.
- You can't share a firewall that's attached to a transit gateway via RAM. To enable
  cross-account access for transit gateway-attached firewalls, share the transit gateway
  itself instead. For more information, see
  [Create a transit gateway-attached firewall](create-tgw-firewall.md "create-tgw-firewall.md").
  For additional details on shareable Network Firewall resources, see [Shareable resources](../../../ram/latest/userguide/shareable.md#shareable-network-firewall "../../../ram/latest/userguide/shareable.md#shareable-network-firewall") in the
  _AWS RAM User Guide_.

###### Contents

- [Prerequisites for sharing Network Firewall resources](#sharing-prereqs "#sharing-prereqs")
- [Related services](#sharing-related "#sharing-related")
- [Sharing across Availability Zones](#sharing-azs "#sharing-azs")
- [Sharing a Network Firewall resource](#sharing-share "#sharing-share")
- [Unsharing a shared Network Firewall resource](#sharing-unshare "#sharing-unshare")
  The owner of a rule group can share a rule group that refers to a [resource group](resource-groups.md "resource-groups.md"), but can't share the resource group itself.

## Prerequisites for sharing AWS Network Firewall resources

- To share a firewall, firewall policy, or rule group, you must own it in your AWS account. You
  cannot share a firewall, firewall policy, or rule group that has been shared with you.
- To share a firewall, firewall policy, or rule group with your organization or an organizational
  unit in AWS Organizations, you must enable sharing with AWS Organizations. For more information,
  see [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
  _AWS RAM User Guide_.

## Related services

Firewall, firewall policy, and rule group sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is
a service that enables you to share your AWS resources with any AWS account or
through AWS Organizations. With AWS RAM, you share resources that you own by creating a
_resource share_. A resource share specifies the resources to
share, and the consumers with whom to share them. Consumers can be individual AWS accounts, organizational units, or an entire organization in AWS Organizations.

For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

## Sharing across Availability Zones

To ensure that resources are distributed across the Availability Zones for a Region,
we independently map Availability Zones to names for each account. This could lead to
Availability Zone naming differences across accounts. For example, the Availability Zone
`us-east-1a` for your AWS account might not have the same location as
`us-east-1a` for another AWS account.

To identify the location of your firewall, firewall policy, or rule group relative to your accounts,
you must use the _Availability Zone ID_ (AZ ID). The AZ ID is a
unique and consistent identifier for an Availability Zone across all AWS accounts. For
example, `use1-az1` is an AZ ID for the `us-east-1` Region and it
is the same location in every AWS account.

###### To view the AZ IDs for the Availability Zones in your account

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home").
2. The AZ IDs for the current Region are displayed in the **Your AZ
   ID** panel on the right-hand side of the screen.

## Sharing an AWS Network Firewall resource

To share a firewall, firewall policy, or rule group, you must add it to a resource share. A resource
share is an AWS RAM resource that lets you share your resources across AWS accounts. A
resource share specifies the resources to share, and the consumers with whom they are
shared. When you share a firewall, firewall policy, or rule group using AWS Network Firewall, you add it to
an existing resource share. To add the firewall, firewall policy, or rule group to a new resource share,
you must first create the resource share using the [AWS RAM console](https://console.aws.amazon.com/ram "https://console.aws.amazon.com/ram").

If you are part of an organization in AWS Organizations and sharing within your organization is
enabled, consumers in your organization are automatically granted access to the shared
firewalls, firewall policies, and rule groups. Otherwise, consumers receive an invitation to join the
resource share and are granted access to the shared firewalls, firewall policies, and rule groups after
accepting the invitation.

You can share any Network Firewall resource that you own using the AWS RAM console, the
AWS Network Firewall API, or the AWS CLI.

###### To share a firewall, firewall policy, or rule group that you own using the AWS RAM console

See [Creating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create") in the
_AWS RAM User Guide_.

###### To share a firewall, firewall policy, or rule group that you own using the AWS CLI

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

###### To share a firewall, firewall policy, or rule group that you own using the Network Firewall

API

Use the `PutResourcePolicy` action. For information about how to use
this, see [PutResourcePolicy](../APIReference/API_PutResourcePolicy.md "../APIReference/API_PutResourcePolicy.md") in the _AWS Network Firewall API
Reference_.

You can see the sharing status of the firewalls that you own in the Network Firewall console on the firewall details page.

## Unsharing a shared AWS Network Firewall resource

When a firewall owner unshares a firewall, the following rules apply:

- Existing VPC endpoint associations remain functional
- The shared account (VPC endpoint association's account) cannot access or view firewall metadata
- VPC endpoint association owners can still delete their associations
- The firewall owner cannot delete their firewall until all VPC endpoint associations are deleted

To unshare a shared firewall, firewall policy, or rule group that you own, you must remove it from the
resource share. You can do this using the AWS RAM console or the AWS CLI.

For more information about the impacts of unsharing a firewall, see [Considerations for working with firewalls and firewall endpoints](firewall-and-firewall-endpoints-considerations.md "firewall-and-firewall-endpoints-considerations.md").

###### To unshare a shared firewall, firewall policy, or rule group that you own using the AWS RAM console

See [Updating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

###### To unshare a shared firewall, firewall policy, or rule group that you own using the AWS CLI

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.
