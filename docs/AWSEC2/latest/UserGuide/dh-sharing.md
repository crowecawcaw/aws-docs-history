# Cross-account Amazon EC2 Dedicated Host sharing

Dedicated Host sharing enables Dedicated Host owners to share their Dedicated Hosts with other AWS accounts or
within an AWS organization. This enables you to create and manage Dedicated Hosts centrally, and
share the Dedicated Host across multiple AWS accounts or within your AWS organization.

In this model, the AWS account that owns the Dedicated Host (_owner_)
shares it with other AWS accounts (_consumers_). Consumers can
launch instances onto Dedicated Hosts that are shared with them in the same way that they would
launch instances onto Dedicated Hosts that they allocate in their own account. The owner is
responsible for managing the Dedicated Host and the instances that they launch onto it. Owners
can't modify instances that consumers launch onto shared Dedicated Hosts. Consumers are
responsible for managing the instances that they launch onto Dedicated Hosts shared with them.
Consumers can't view or modify instances owned by other consumers or by the Dedicated Host owner,
and they can't modify Dedicated Hosts that are shared with them.

A Dedicated Host owner can share a Dedicated Host with:

- Specific AWS accounts inside or outside of its AWS organization
- An organizational unit inside its AWS organization
- Its entire AWS organization

###### Contents

- [Prerequisites for sharing Dedicated Hosts](#dh-sharing-prereq "#dh-sharing-prereq")
- [Limitations for sharing Dedicated Hosts](#dh-sharing-limitation "#dh-sharing-limitation")
- [Related services](#dh-sharing-related "#dh-sharing-related")
- [Share across Availability Zones](#dh-sharing-azs "#dh-sharing-azs")
- [Shared Dedicated Host permissions](#shared-dh-perms "#shared-dh-perms")
- [Billing and metering](#shared-dh-billing "#shared-dh-billing")
- [Dedicated Host limits](#shared-dh-limits "#shared-dh-limits")
- [Host recovery and Dedicated Host sharing](#dh-sharing-retirement "#dh-sharing-retirement")
- [Share a Dedicated Host](sharing-dh.md "sharing-dh.md")
- [Unshare a Dedicated Host](unsharing-dh.md "unsharing-dh.md")
- [View shared Dedicated Hosts](identifying-shared-dh.md "identifying-shared-dh.md")

## Prerequisites for sharing Dedicated Hosts

- To share a Dedicated Host, you must own it in your AWS account. You can't share a
  Dedicated Host that has been shared with you.
- To share a Dedicated Host with your AWS organization or an organizational unit in
  your AWS organization, you must enable sharing with AWS Organizations. For more
  information, see [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the _AWS RAM User Guide_.

## Limitations for sharing Dedicated Hosts

You can't share Dedicated Hosts that have been allocated for the following instance types:
`u-6tb1.metal`, `u-9tb1.metal`,
`u-12tb1.metal`, `u-18tb1.metal`, and
`u-24tb1.metal`.

## Related services

### AWS Resource Access Manager

Dedicated Host sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is a service that
enables you to share your AWS resources with any AWS account or through
AWS Organizations. With AWS RAM, you share resources that you own by creating a
_resource share_. A resource share specifies the
resources to share, and the consumers with whom to share them. Consumers can be
individual AWS accounts, or organizational units or an entire organization
from AWS Organizations.

For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

## Share across Availability Zones

To ensure that resources are distributed across the Availability Zones for a
Region, we independently map Availability Zones to names for each account. This
could lead to Availability Zone naming differences across accounts. For example, the
Availability Zone `us-east-1a` for your AWS account might not have the
same location as `us-east-1a` for another AWS account.

To identify the location of your Dedicated Hosts relative to your accounts, you must use the
_Availability Zone ID_ (AZ ID). The Availability Zone ID is a
unique and consistent identifier for an Availability Zone across all AWS accounts.
For example, `use1-az1` is an Availability Zone ID for the
`us-east-1` Region and it is the same location in every AWS
account.

###### To view the Availability Zone IDs for the Availability Zones in your

account

1. Open the AWS RAM console at [https://console.aws.amazon.com/ram/home](https://console.aws.amazon.com/ram/home "https://console.aws.amazon.com/ram/home").
2. The Availability Zone IDs for the current Region are displayed in the
   **Your AZ ID** panel on the right-hand side of the
   screen.

## Shared Dedicated Host permissions

### Permissions for owners

Owners are responsible for managing their shared Dedicated Hosts and the instances that
they launch onto them. Owners can view all instances running on the shared Dedicated Host,
including those launched by consumers. However, owners can't take any action on
running instances that were launched by consumers.

### Permissions for consumers

Consumers are responsible for managing the instances that they launch onto a
shared Dedicated Host. Consumers can't modify the shared Dedicated Host in any way, and they can't
view or modify instances that were launched by other consumers or the Dedicated Host
owner.

## Billing and metering

There are no additional charges for sharing Dedicated Hosts.

Owners are billed for Dedicated Hosts that they share. Consumers are not billed for
instances that they launch onto shared Dedicated Hosts.

Dedicated Host Reservations continue to provide billing discounts for shared Dedicated Hosts. Only Dedicated Host owners
can purchase Dedicated Host Reservations for shared Dedicated Hosts that they own.

## Dedicated Host limits

Shared Dedicated Hosts count towards the owner's Dedicated Hosts limits only. Consumer's Dedicated Hosts limits
are not affected by Dedicated Hosts that have been shared with them. Similarly, instances that
consumers launch onto shared Dedicated Hosts do not count towards their instance
limits.

## Host recovery and Dedicated Host sharing

Host recovery recovers instances launched by the Dedicated Host owner and the consumers with
whom it has been shared. The replacement Dedicated Host is allocated to the owner's account.
It is added to the same resource shares as the original Dedicated Host, and it is shared with
the same consumers.

For more information, see [Amazon EC2 Dedicated Host recovery](dedicated-hosts-recovery.md "dedicated-hosts-recovery.md").
