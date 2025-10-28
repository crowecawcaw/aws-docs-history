# Mounting EFS file systems from

another AWS account or VPC

You can mount your EFS file system using IAM authorization for NFS clients
and EFS access points using the EFS mount helper. By default, the
EFS mount helper uses domain name service (DNS) to resolve the IP address of your
EFS mount target. If you are mounting the file system from a different account or
virtual private cloud (VPC), you need to resolve the EFS mount target
manually.

Following, you can find instructions for determining the correct EFS mount
target IP address to use for your NFS client. You can also find instructions for configuring
the client to mount the EFS file system using that IP address.

###### Topics

- [Mounting EFS file systems from another AWS account](mount-fs-diff-account-same-vpc.md "mount-fs-diff-account-same-vpc.md")
- [Mounting EFS file systems from another
  VPC](mount-fs-different-vpc.md "mount-fs-different-vpc.md")
