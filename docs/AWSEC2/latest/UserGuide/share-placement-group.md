# Shared placement groups

Placement group sharing allows you to influence the placement of interdependent
instances that are owned by separate AWS accounts. An owner can share a placement group
across multiple AWS accounts or within their organization. A participant can launch
instances in a placement group that is shared with their account.

A placement group owner can share a placement group with:

- Specific AWS accounts inside or outside of its organization
- An organizational unit inside its organization
- Its entire organization
  You can use VPC peering to connect instances owned by separate AWS accounts and get
  the full latency benefits offered by shared cluster placement groups.

###### Contents

- [Rules and limitations](#share-placement-group-limitations "#share-placement-group-limitations")
- [Required permissions](#share-placement-group-permissions "#share-placement-group-permissions")
- [Sharing across Availability Zones](#share-placement-group-sharing-azs "#share-placement-group-sharing-azs")
- [Placement group sharing](#share-placement-group-share "#share-placement-group-share")
- [Placement group unsharing](#share-placement-group-unshare "#share-placement-group-unshare")

## Rules and limitations

The following rules and limitations apply when you share a placement group or when
a placement group is shared with you.

- To share a placement group, you must own it in your AWS account. You
  can't share a placement group that has been shared with you.
- When you share a partition or spread placement group, the placement group
  limits do not change. A shared partition placement group supports a maximum
  of seven partitions per Availability Zone, and a shared spread placement
  group supports a maximum of seven running instances per Availability
  Zone.
- To share a placement group with your organization or an organizational
  unit in your organization, you must enable sharing with AWS Organizations. For more
  information, see [Sharing your
  AWS resources](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md").
- When using the AWS Management Console to launch an instance, you can select any
  placement groups that were shared with you. When using the AWS CLI to launch
  an instance, you must specify a shared placement group by ID, not by name.
  You can use the name of a placement group only if you're the owner of the
  shared placement group.
- You are responsible for managing the instances owned by you in a shared
  placement group.
- You can't view or modify instances and capacity reservations that are
  associated with a shared placement group but not owned by you.
- The Amazon Resource Name (ARN) of a placement group contains the ID of
  the account that owns the placement group. You can use the account ID
  portion of a placement group ARN to identify the owner of a placement
  group that is shared with you.

## Required permissions

To share a placement group, users must have permissions for following actions:

- `ec2:PutResourcePolicy`
- `ec2:DeleteResourcePolicy`

## Sharing across Availability Zones

To ensure that resources are distributed across the Availability Zones for a
Region, we independently map Availability Zones to names for each account. This
could lead to Availability Zone naming differences across accounts. For example, the
Availability Zone `us-east-1a` for your AWS account might not have the
same location as `us-east-1a` for another AWS account.

To specify the location of your Dedicated Hosts relative to your accounts, you
must use the _Availability Zone ID_ (AZ ID). The AZ ID is a
unique and consistent identifier for an Availability Zone across all AWS
accounts. For example, `use1-az1` is an Availability Zone ID for
the `us-east-1` Region and it is the same location in every AWS
account. For more information, see [AZ IDs](../../../global-infrastructure/latest/regions/az-ids.md "../../../global-infrastructure/latest/regions/az-ids.md").

## Placement group sharing

To share a placement group, you must add it to a resource share. A resource share
is an AWS RAM resource that lets you share your resources across AWS accounts. A
resource share specifies the resources to share, and the consumers with whom they
are shared.

If you are part of an organization in AWS Organizations sharing within your organization is
enabled, consumers in your organization are granted access to the shared placement
group.

If the placement group is shared with an AWS account outside of your
organization, the AWS account owner will receive an invitation to join the
resource share. They can access the shared placement group after accepting the
invitation.

You can share a placement group across AWS accounts using AWS Resource Access Manager. For more
information, see [Creating a resource share](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS RAM User Guide_.

## Placement group unsharing

The placement group owner can unshare a shared placement group at any time.
When you unshare a shared placement group, the following changes occur:

- The AWS accounts with which a placement group was shared are no longer
  able to launch instances or reserve capacity.
- Any instances running in a shared placement group are disassociated
  from the placement group, but they continue to run in your AWS account.
- Any capacity reservations in a shared placement group are disassociated
  from the placement group, but remain available to you in your AWS account.

For more information, see [Deleting a resource share](../../../ram/latest/userguide/working-with-sharing-delete.md "../../../ram/latest/userguide/working-with-sharing-delete.md") in the _AWS RAM User Guide_.
