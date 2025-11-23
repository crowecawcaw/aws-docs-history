# You can't access your file system

This section describes issues and resolutions related to being unable to access your file system.

###### Topics

- [Your Multi-AZ file system has missing route table tags](#no-route-table-tags "#no-route-table-tags")
- [Your file system has more than 50 routes](#more-than-50-routes "#more-than-50-routes")
- [Your file system is missing routes to one or more file servers](#missing-routes-to-servers "#missing-routes-to-servers")
- [The file system's elastic network interface was modified or
  deleted](#eni-deleted "#eni-deleted")
- [The Elastic IP address attached to the file system's elastic network interface was deleted](#eni-epi-removed "#eni-epi-removed")
- [The file system's VPC security group lacks the required inbound
  rules](#sg-lacks-inbound-rules "#sg-lacks-inbound-rules")
- [The compute instance's VPC security group lacks the
  required outbound rules](#compute-instance-lacks-inbound-rules "#compute-instance-lacks-inbound-rules")
- [The compute instance's subnet doesn't use any of the route tables associated with your file system](#subnet-route-tables "#subnet-route-tables")
- [Amazon FSx can't update route table for Multi-AZ file systems created using CloudFormation](#vpc-route-tables-not-tagged "#vpc-route-tables-not-tagged")
- [Can't access a file system over iSCSI from a client in another VPC](#file-system-iscsi "#file-system-iscsi")
- [The owning account has stopped sharing the VPC subnet](#unshared-vpc-subnet "#unshared-vpc-subnet")
- [Can't access a file system over NFS, SMB, the ONTAP CLI,
  or the ONTAP REST API from a client in another VPC or on-premises](#unable-to-access-over-network "#unable-to-access-over-network")

## Your Multi-AZ file system has missing route table tags

Amazon FSx manages VPC route tables for Multi-AZ file systems using tag-based authentication. One or more
of the route tables associated with your file system are currently missing these route table
tags. These route tables are tagged with `Key: AmazonFSx; Value: ManagedByAmazonFSx`.
If you do not manually add these tags before the next maintenance window, any clients in subnets associated
with the route tables that are missing the tags will temporarily lose access to the file system for duration
of the patching operation. To avoid this, please manually add the missing route table tags.

For more information, see [Updating file systems](updating-file-system.md "updating-file-system.md").

## Your file system has more than 50 routes

Your file system currently has more than 50 routes associated with it. If you do not remove some of these routes
before your file system’s next scheduled maintenance window, the failover process may take longer than normal. To
avoid this, please reduce the number of routes to less than 50. The following are steps you can take to reduce the number of
routes associated with your file system:

- Deleting any excess routes
- Reducing the number of SVMs associated with the file system
- Reducing the number of route tables associated with the file system

For more information, see [Updating file systems](updating-file-system.md "updating-file-system.md") and
[Deleting storage virtual machines (SVM)](deleting-svms.md "deleting-svms.md").

## Your file system is missing routes to one or more file servers

Your file system is currently missing routes to one or more file servers, and the existing route tables do not have sufficient
space to add new route table entries. If you do not add the missing routes before your file system’s next scheduled maintenance window,
any connected clients will be disconnected for the duration of the patching operation. To avoid this, please add the missing routes.

For more information, see [Updating file systems](updating-file-system.md "updating-file-system.md") and
[Quotas](limits.md "limits.md").

## The file system's elastic network interface was modified or

deleted

You must not modify or delete any of the file system's elastic network interfaces.
Modifying or deleting a network interface can cause a permanent loss of connection between your
virtual private cloud (VPC) and your file system. Create a new file system, and don't modify or
delete the Amazon FSx network interface. For more information, see [File System Access Control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").

## The Elastic IP address attached to the file system's elastic network interface was deleted

Amazon FSx doesn't support accessing file systems from the public Internet. Amazon FSx
automatically detaches any Elastic IP address which is a public IP address
reachable from the Internet that gets attached to a file system's elastic
network interface. For more information, see [Supported clients](supported-fsx-clients.md#supported-clients-fsx "supported-fsx-clients.md#supported-clients-fsx").

## The file system's VPC security group lacks the required inbound

rules

Review the inbound rules specified in [Amazon VPC security groups](limit-access-security-groups.md#fsx-vpc-security-groups "limit-access-security-groups.md#fsx-vpc-security-groups"), and make sure that the security group
associated with your file system has the corresponding inbound rules.

## The compute instance's VPC security group lacks the

required outbound rules

Review the outbound rules specified in [Amazon VPC security groups](limit-access-security-groups.md#fsx-vpc-security-groups "limit-access-security-groups.md#fsx-vpc-security-groups"), and make sure that the security group
associated with your compute instance has the corresponding outbound rules.

## The compute instance's subnet doesn't use any of the route tables associated with your file system

FSx for ONTAP creates endpoints for accessing your file system in a VPC route table. We
recommend that you configure your file system to use all of the VPC route tables that are
associated with the subnets in which your clients are located. By default, Amazon FSx uses your
VPC's main route table. You can optionally specify one or more route tables for Amazon FSx to
use when you create your file system.

If you can ping your file system's Intercluster endpoint but cannot ping your file
system's Management endpoint (see [File system resources](managing-file-systems.md#fsx-ontap-fs-resources "managing-file-systems.md#fsx-ontap-fs-resources") for more information), your client is likely not in a
subnet that's associated with one of your file system's route tables. To access your
file system, associate one of your file system's route tables with your client's
subnet. For information about updating your file system's Amazon VPC route tables, see
[Updating file systems](updating-file-system.md "updating-file-system.md").

## Amazon FSx can't update route table for Multi-AZ file systems created using CloudFormation

Amazon FSx manages VPC route tables for Multi-AZ file systems using tag-based authentication.
These route tables are tagged with `Key: AmazonFSx; Value: ManagedByAmazonFSx`.
When creating or updating FSx for ONTAP Multi-AZ file systems using CloudFormation we recommend that you add the
`Key: AmazonFSx; Value: ManagedByAmazonFSx` tag manually.

If you're unable to reach your Multi-AZ file system, check to see if the VPC route tables
associated with the file system are tagged with `Key: AmazonFSx; Value: ManagedByAmazonFSx`.
If they are not, then Amazon FSx cannot update those route tables to route the floating IP addresses of the
management and data ports to the active file server when a failover event occurs.
For information about updating your file system's Amazon VPC route tables, see
[Updating file systems](updating-file-system.md "updating-file-system.md").

## Can't access a file system over iSCSI from a client in another VPC

To access a file system over the Internet Small Computer Systems Interface (iSCSI) protocol
from a client in another VPC, you can configure Amazon VPC peering or AWS Transit Gateway
between the VPC associated with your file system and the VPC in which your client resides. For
more information, see [Create and accept VPC peering
connections](../../../vpc/latest/peering/create-vpc-peering-connection.md "../../../vpc/latest/peering/create-vpc-peering-connection.md") in the _Amazon Virtual Private Cloud_ guide.

## The owning account has stopped sharing the VPC subnet

If you created your file system in a VPC subnet that has been shared with you, the owning account may have stopped sharing the
VPC subnet.

If the owner account has stopped sharing the VPC subnet, you will see the following message in the console for that file system:

```
The vpc ID `vpc-012345abcde` does not exist
```

You will need to contact the owning account so that they can re-share the subnet with you.

## Can't access a file system over NFS, SMB, the ONTAP CLI,

or the ONTAP REST API from a client in another VPC or on-premises

To access a file system over Network File System (NFS), Server Message Block (SMB), or the
NetApp ONTAP CLI and REST API from a client in another VPC or on premises, you must configure
routing using AWS Transit Gateway between the VPC associated with your file system
and the network in which your client resides. For more information, see [Accessing your FSx for ONTAP data](supported-fsx-clients.md "supported-fsx-clients.md").
