# Shared multicast domains in AWS Transit Gateway

With multicast domain sharing, multicast domain owners can share the domain with other AWS
accounts inside its organization or across organizations in AWS Organizations. As the multicast
domain owner, you can create and manage the multicast domain centrally. Once shared, those
users can perform the following operations on a shared multicast domain:

- Register and deregister group members or group sources in the multicast
  domain
- Associate a subnet with the multicast domain, and disassociate subnets from the multicast
  domain
  A multicast domain owner can share a multicast domain with:

- AWS accounts inside its organization or across organizations in AWS Organizations
- An organizational unit inside its organization in AWS Organizations
- Its entire organization in AWS Organizations
- AWS accounts outside of AWS Organizations.

To share a multicast domain with an AWS account outside of your Organization, you must
create a resource share using AWS Resource Access Manager, and then choose **Allow
sharing with anyone** when selecting the Principals to share the
multicast domain with. For more information on creating a resource share, see [Creating a resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS RAM User Guide_

###### Contents

- [Prerequisites for sharing a multicast domain](#sharing-prereqs "#sharing-prereqs")
- [Related services](#sharing-related "#sharing-related")
- [Shared multicast domain permissions](#sharing-perms "#sharing-perms")
- [Billing and metering](#sharing-billing "#sharing-billing")
- [Quotas](#sharing-quotas "#sharing-quotas")
- [Share resources across Availability Zones](sharing-azs.md "sharing-azs.md")
- [Share a multicast domain](sharing-share.md "sharing-share.md")
- [Unshare a shared multicast domain](sharing-unshare.md "sharing-unshare.md")
- [Identify a shared multicast domain](sharing-identify.md "sharing-identify.md")

## Prerequisites for sharing a multicast domain

- To share a multicast domain, you must own it in your AWS account. You cannot share a multicast domain
  that has been shared with you.
- To share a multicast domain with your organization or an organizational unit in AWS Organizations, you
  must enable sharing with AWS Organizations. For more information, see [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.

## Related services

Multicast domain sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is a service that enables
you to share your AWS resources with any AWS account or through AWS Organizations. With
AWS RAM, you share resources that you own by creating a _resource
share_. A resource share specifies the resources to share, and the users
with whom to share them. Consumers can be individual AWS accounts, or organizational
units or an entire organization in AWS Organizations.

For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

## Shared multicast domain permissions

### Permissions for owners

Owners are responsible for managing the multicast domain and the members and attachments
that they register or associate with the domain. Owners can change or revoke shared
access at any time. They can use AWS Organizations to view, modify, and delete
resources that consumers create on shared multicast domains.

### Permissions for consumers

Users of the shared multicast domain can perform the following operations on shared
multicast domains in the same way that they would on multicast domains that they
created:

- Register and deregister group members or group sources in the multicast
  domain
- Associate a subnet with the multicast domain, and disassociate subnets from the multicast
  domain

Consumers are responsible for managing the resources that they create on the shared
multicast domain.

Customers cannot view or modify resources owned by other consumers or by the
multicast domain owner, and they cannot modify multicast domains that are shared
with them.

## Billing and metering

There are no additional charges for sharing multicast domains for either the owner, or
consumers.

## Quotas

A shared multicast domain counts toward the owner's and shared user's multicast domain
quotas.
