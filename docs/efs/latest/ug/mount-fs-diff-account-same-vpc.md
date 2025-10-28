# Mounting EFS file systems from another AWS account

Using shared VPCs, you can mount an EFS file system that is owned by one
AWS account from Amazon EC2 instances that are owned by a different AWS account. For more
information about setting up a shared VPC, see [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md")
in the _Amazon VPC Peering Guide_.

After you set up VPC sharing, the EC2 instances can mount the EFS
file system using Domain Name System (DNS) name resolution or the EFS mount
helper. We recommend using the EFS mount helper to mount your EFS
file systems.
