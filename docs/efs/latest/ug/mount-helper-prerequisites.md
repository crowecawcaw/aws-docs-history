# Prerequisites for using the EFS mount

helper

You can mount an EFS file system on an Amazon EC2 instance using the Amazon EFS mount
helper. To use the mount helper, you need the following:

- **File system ID of the file system to mount** - The
  EFS mount helper resolves the file system ID to the local IP address of the
  mount target elastic network interface (ENI) without calling external resources.
- **An EFS mount target**
  – You create mount targets in your virtual private cloud (VPC). If you create your
  file system in the console using the service recommended settings, a mount target is
  created in each Availability Zone in the AWS Region that the file system is in. For
  instructions to create mount targets, see [Managing mount targets](accessing-fs.md "accessing-fs.md").

###### Note

We recommend that you wait 60 seconds after the newly created mount target's
lifecycle state is **available** before mounting the file system via
DNS. This wait lets the DNS records propagate fully in the AWS Region where the file
system resides.

If you use a mount target in an Availability Zone different from that of your EC2
instance, you incur standard EC2 charges for data sent across Availability Zones. You
also might see increased latencies for file system operations.

- For mounting One Zone file systems from a
  different Availability Zone:
  - **The name of the file system's Availability Zone** – If you are
    mounting an EFS One Zone file system that is located in a
    different Availability Zone than the EC2 instance.
  - **Mount target DNS name** – Alternatively, you can specify
    the mount target's DNS name instead of the Availability Zone.

- **An EC2 instance running one of the supported Linux or
  macOS distributions** – The supported distributions for mounting your
  file system with the mount helper are the following:
  - Amazon Linux 2
  - Amazon Linux 2023
  - Amazon Linux 2017.09 and newer
  - macOS Big Sur
  - Red Hat Enterprise Linux (and derivatives such as CentOS) version 7 and
    newer
  - Ubuntu 16.04 LTS and newer

###### Note

EC2 Mac instances running macOS Big Sur support NFS 4.0 only.

- **The EFS mount helper is installed on the EC2
  instance** – The mount helper is a tool in the
  `amazon-efs-utils` package of utilities. For information about
  installing `amazon-efs-utils`, see [Installing the Amazon EFS client](using-amazon-efs-utils.md "using-amazon-efs-utils.md").
- **The EC2 instance is in a VPC** – The
  connecting EC2 instance must be in a virtual private cloud (VPC) based on the
  Amazon VPC service. It also must be configured to use the DNS server provided by AWS. For
  information about the Amazon DNS server, see [DHCP option sets in Amazon VPC](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in the
  _Amazon VPC User Guide_.
- **VPC has DNS hostnames enabled** – The VPC of
  the connecting EC2 instance must have DNS hostnames enabled. For more
  information, see [DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-viewing "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-viewing") in the
  _Amazon VPC User Guide_.
- **For EC2 instances and file systems in different
  AWS Regions** – If the EC2 instance and the file system you
  are mounting are located in different AWS Regions, you will need to edit the
  `region` property in the `efs-utils.conf` file. For more
  information, see [Mounting EFS file systems from a different AWS Region](mount-different-region.md "mount-different-region.md").
