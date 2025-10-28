# Responsibilities and permissions for owners and

participants

This section includes details about the responsibilities and permissions for those who own the shared subnet (owner) and for those who are using the shared subnet (participant).

## Owner resources

Owners are responsible for the VPC resources that they own. VPC owners are responsible for creating, managing, and deleting the resources associated
with a shared VPC. These include subnets, route tables, network ACLs, peering connections,
gateway endpoints, interface endpoints, Route 53 Resolver endpoints, internet
gateways, NAT gateways, virtual private gateways, and transit gateway attachments.

## Participant resources

Participants are responsible for the VPC resources that they own. Participants can create a limited set of VPC resources in a shared VPC. For example,
participants can create network interfaces and security groups, and enable VPC flow logs for
the network interfaces that they own. The VPC resources that a participant creates count
against the VPC quotas in the participant account, not the owner account. For more information, see [VPC subnet sharing](amazon-vpc-limits.md#vpc-share-limits "amazon-vpc-limits.md#vpc-share-limits").

## VPC resources

The following responsibilities and permissions apply to VPC resources when working with shared VPC subnets:

###### Flow logs

- Participants can create, delete, and describe flow logs for network interfaces
  that they own in a shared VPC subnet.
- Participants cannot create, delete, or describe flow logs for network interfaces
  that they do not own in a shared VPC subnet.
- Participants cannot create, delete, or describe flow logs for a shared VPC
  subnet.
- VPC owners can create, delete, and describe flow logs for network interfaces
  that they do not own in a shared VPC subnet.
- VPC owners can create, delete, and describe flow logs for a shared VPC
  subnet.
- VPC owners cannot describe or delete flow logs created by a participant.

###### Internet gateways and egress-only internet gateways

- Participants cannot create, attach, or delete internet gateways and egress-only internet
  gateways in a shared VPC subnet. Participants can describe internet gateways in a shared
  VPC subnet. Participants cannot describe egress-only internet gateways in a shared VPC
  subnet.

###### NAT gateways

- Participants cannot create, delete, or describe NAT gateways in a shared VPC subnet.

###### Network access control lists (NACLs)

- Participants cannot create, delete, or replace NACLs in a shared VPC subnet. Participants can describe NACLs created by VPC owners in a shared VPC subnet.

###### Network interfaces

- Participants can create network interfaces in a shared VPC subnet. Participants cannot work with network interfaces created by VPC owners in a shared VPC subnet in any other way, such as attaching, detaching, or modifying the network interfaces. Participants can modify or delete the network interfaces in a shared VPC that they created. For example, participants can associate or disassociate IP addresses with the network interfaces that they created.
- VPC owners can describe network interfaces owned by participants in a shared VPC subnet. VPC
  owners cannot work with network interfaces owned by participants in any other way, such as
  attaching, detaching, or modifying the network interfaces owned by participants in a
  shared VPC subnet.

###### Route tables

- Participants cannot work with route tables (for example, create, delete, or associate route tables) in a shared VPC subnet. Participants can describe route tables in a shared VPC subnet.

###### Security groups

- Participants can work with (create, delete, describe, modify, or create ingress and egress
  rules for) security groups that they own in a shared VPC subnet. Participants can work
  with security groups created by VPC owners if [the VPC owner shares the security group with the participant](security-group-sharing.md "security-group-sharing.md").
- Participants can create rules in the security groups that they own that reference security groups that belong to other participants or the VPC owner as follows: account-number/security-group-id
- Participants can't launch instances using the default security group for the VPC
  because it belongs to the owner.
- Participants can't launch instances using non-default security groups that are owned
  by the VPC owner or other participants unless the security group is [shared with them](security-group-sharing.md "security-group-sharing.md").
- VPC owners can describe the security groups created by participants in a shared VPC subnet.
  VPC owners cannot work with security groups created by participants in any other way.
  For example, VPC owners can't launch instances using security groups created by
  participants.

###### Subnets

- Participants cannot modify shared subnets or their related attributes. Only the VPC owner can. Participants can describe subnets in a shared VPC subnet.
- VPC owners can share subnets only with other accounts or organizational units that are in the same organization from AWS Organizations. VPC owners can't share subnets that are in a default VPC.

###### Transit gateways

- Only the VPC owner can attach a transit gateway to a shared VPC subnet. Participants can't.

###### VPCs

- Participants cannot modify VPCs or their related attributes. Only the VPC owner can. Participants can describe VPCs, their attibutes, and the DHCP option sets.
- VPC tags and tags for the resources within the shared VPC are not shared with the participants.
- Participants can associate their own security groups with a shared VPC. This allows
  the participant to use the security group with Elastic network interfaces they own in
  the shared VPC.
