# Migrating your existing file storage to Amazon FSx for OpenZFS

The following sections provide information on how to migrate your existing file storage to Amazon FSx for OpenZFS
using AWS DataSync, `rsync` or `Robocopy`.

- **AWS DataSync** – An online data transfer service designed
  to simplify, automate, and accelerate copying large amounts of data to and from AWS storage services.
- **rsync** – Remote sync is an open source utility for
  efficiently transferring and synchronizing files commonly available on most Linux or other Unix-based operating systems.
- **Robocopy** – Robust File Copy is a command
  line directory and file replication command set for Microsoft Windows.
  Before you begin using the procedures described in the following sections, be sure that the following prerequisites
  are met:

- You have created a destination FSx for OpenZFS file system. For more information,
  see [Creating an Amazon FSx for OpenZFS file system](creating-file-systems.md "creating-file-systems.md").
- The source and destination file systems are connected in the same virtual private cloud (VPC).
  The source file system can be located on-premises or in another Amazon VPC, AWS account, or AWS Region, but it must be in a
  network peered with that of the destination file system using Amazon VPC Peering, Transit Gateway, AWS Direct Connect,
  or AWS VPN. For more information, see [Access from a different VPC](access-within-aws.md#vpc-peering "access-within-aws.md#vpc-peering") and
  [What is VPC peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md")
  in the _Amazon VPC Peering Guide_.

###### Topics

- [Migrating files with AWS DataSync](migrate-files-to-fsx-datasync.md "migrate-files-to-fsx-datasync.md")
- [Migrating files with rsync](fsx-migrate-rsync.md "fsx-migrate-rsync.md")
- [Migrating files with Robocopy](fsx-migrate-robocopy.md "fsx-migrate-robocopy.md")
- [Cutting over to your file system](cutover.md "cutover.md")
