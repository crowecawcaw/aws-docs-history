# Managing mount targets

You mount your file system on Amazon EC2 or other AWS compute instance in your virtual private
cloud (VPC) using one or more mount targets that you create for the file system. You can
create the mount target when you create the file system or after you create the file system.

After a mount target is created for a file system, you can create additional mount targets,
delete mount targets, and modify the security groups for mount targets. If you want to modify
the VPC for mount targets, then you need to first delete the existing mount targets.

###### Note

You can't change the IP address of an existing mount target. To change an IP address,
you need to delete the mount target and create a new one with the new address.

###### Topics

- [Mount targets and Availability Zones](#about-mount-targets "#about-mount-targets")
- [Creating mount targets](manage-fs-access-create-delete-mount-targets.md "manage-fs-access-create-delete-mount-targets.md")
- [Deleting mount targets](mount-target-delete.md "mount-target-delete.md")
- [Changing the mount target VPC](manage-fs-access-change-vpc.md "manage-fs-access-change-vpc.md")
- [Changing mount target
  security groups](manage-fs-access-update-mount-target-config-sg.md "manage-fs-access-update-mount-target-config-sg.md")

## Mount targets and Availability Zones

For EFS file systems that use Regional storage classes, you can
create a mount target in each Availability Zone in an AWS Region.

For One Zone file systems, you can only create a single mount target in the
same Availability Zone as the file system. Then you can mount the file system on compute instances,
including Amazon EC2, Amazon ECS, and AWS Lambda in your virtual private cloud (VPC).

The following diagram shows a Regional file system with mount targets
created in all Availability Zones in the VPC. The illustration shows three EC2 instances launched in different VPC subnets
accessing an EFS file system. The illustration also shows one mount target in each of the Availability Zones
(regardless of the number of subnets in each Availability Zone).

You can create only one mount target per Availability Zone. If an Availability Zone has multiple subnets, as
shown in one of the zones in the illustration, you create a mount target in only one of the subnets. As long as
you have one mount target in an Availability Zone, the EC2 instances launched in any of its subnets can share the
same mount target.

![Regional file system with mount targets in three Availability Zones within a VPC on EC2 instances.](images/efs-ec2-how-it-works-Regional_china-world.png)

The following diagram shows a One Zone file system, with a
single mount target created in the same Availability Zone as the file system. Accessing the file
system by using the EC2 instance in the `us-west2c` Availability Zone incurs data
access charges because it is located in a different Availability Zone than the mount target.

![One Zone file system with a single mount target created in the same Availability Zone.](images/efs-ec2-how-it-works-OneZone.png)

The mount target security group acts as a virtual firewall that controls the traffic. For
example, it determines which clients can access the file system. This section explains the
following:

- Managing mount target security groups and enabling traffic.
- Mounting the file system on your clients.
- NFS-level permissions considerations.

Initially, only the root user on the Amazon EC2 instance has read-write-execute permissions
on the file system. This topic discusses NFS-level permissions and provides examples that
show you how to grant permissions in common scenarios. For more information, see [Network File System (NFS) level users, groups, and permissions](accessing-fs-nfs-permissions.md "accessing-fs-nfs-permissions.md").
