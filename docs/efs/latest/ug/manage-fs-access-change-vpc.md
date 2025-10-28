# Changing the mount target VPC

You can use an EFS file system in one VPC based on the Amazon VPC service at a time. That
is, you create mount targets in a VPC for your file system, and use those mount targets to
provide access to the file system.

You can mount the EFS file system from these targets:

- Amazon EC2 instances in the same VPC
- EC2 instances in a VPC connected by VPC peering
- On-premises servers by using AWS Direct Connect
- On-premises servers over an AWS virtual private network (VPN) by using Amazon VPC
  A _VPC peering connection_ is a networking connection
  between two VPCs that enables you to route traffic between them. The connection can use
  private Internet Protocol version 4 (IPv4) or version 6 (IPv6).
  For more information on how Amazon EFS works with VPC peering, see [Mounting EFS file systems from
  another AWS account or VPC](manage-fs-access-vpc-peering.md "manage-fs-access-vpc-peering.md").

###### To change the VPC for a file system

The following are the steps that you'll perform to change the VPC for an
EFS file system's network configuration.

1. Delete each mount target assigned to the file system. For instructions, see
   [Deleting mount targets](mount-target-delete.md "mount-target-delete.md").
2. When the **Mount targets status** for each mount target is
   **Deleted**, assign the new VPC and create new mount targets for
   the file system. For instructions, see [Creating mount targets](manage-fs-access-create-delete-mount-targets.md "manage-fs-access-create-delete-mount-targets.md").
