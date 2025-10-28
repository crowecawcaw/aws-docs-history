# Mounting EFS file systems using the

EFS mount helper

After you install the Amazon EFS client (`amazon-efs-utils`), you can use
the EFS mount helper to mount EFS file systems on your EC2 Linux and Mac
instances running a [supported distributions](using-amazon-efs-utils.md#efs-utils-supported-distros "using-amazon-efs-utils.md#efs-utils-supported-distros").
Amazon EFS does not support mounting from EC2 Windows instances.

###### Important

We recommend that you always use the most current version of
`amazon-efs-utils` to ensure successful mounting. For example, versions
of `amazon-efs-utils` prior to 2.3 do not support mounting with IPv6
addresses.

When mounting a file system, the mount helper defines a new network file system
type, called `efs`, which is fully compatible with the standard `mount`
command in Linux. The mount helper also supports mounting an EFS file system at
instance boot time automatically by using entries in the `/etc/fstab`
configuration file on EC2 Linux instances.

###### Warning

Use the `_netdev` option, used to identify network file systems, when
mounting your file system automatically. If `_netdev` is missing, your EC2
instance might stop responding. This result is because network file systems need to be
initialized after the compute instance starts its networking. For more information, see
[Automatic mounting fails and the instance is
unresponsive](troubleshooting-efs-mounting.md#automount-fails "troubleshooting-efs-mounting.md#automount-fails").

You can mount a file system by specifying one of the following properties:

- **File system DNS name** – If you use the file system DNS name,
  and the mount helper cannot resolve it, for example when you are mounting
  a file system in a different VPC, it will fall back to using the mount target IP address. For more information, see
  [Mounting EFS file systems from
  another AWS account or VPC](manage-fs-access-vpc-peering.md "manage-fs-access-vpc-peering.md").
- **File system ID** – If you use the file system ID, the mount helper resolves it to the
  local IP address of the mount target elastic network interface (ENI) without calling external resources.
- **Mount target IP address** – You can use the IP address of one of the file systems mount targets.
  You can find the value for all of these properties in the Amazon EFS console. The file system
  DNS name is found in the **Attach** screen.

When encryption of data in transit is declared as a mount option for your EFS
file system, the mount helper initializes a client `stunnel` process, and a
supervisor process called `amazon-efs-mount-watchdog`. The
`amazon-efs-mount-watchdog` process monitors the health of TLS mounts, and is
started automatically the first time an EFS file system is mounted over TLS. If
your client is running on Linux, this process is managed by either
`upstart` or `systemd` depending on your Linux
distribution. For clients running on a supported macOS, it is managed by
`launchd`.

`Stunnel` is an open-source multipurpose network relay. The client `stunnel` process listens
on a local port for inbound traffic, and the mount helper redirects NFS client traffic to this local port.

The mount helper uses TLS version 1.2 to communicate with your file system. Using TLS requires certificates,
and these certificates are signed by a trusted Amazon Certificate Authority. For more information on how encryption works, see [Data encryption in Amazon EFS](encryption.md "encryption.md").

###### Topics

- [Mount settings used by EFS mount helper](mount-helper-setting.md "mount-helper-setting.md")
- [Getting support logs](mount-helper-logs.md "mount-helper-logs.md")
- [Prerequisites for using the EFS mount
  helper](mount-helper-prerequisites.md "mount-helper-prerequisites.md")
- [Mounting on EC2 Linux instances
  using the EFS mount helper](mounting-fs-mount-helper-ec2-linux.md "mounting-fs-mount-helper-ec2-linux.md")
- [Mounting on EC2 Mac instances
  using the EFS mount helper](mounting-fs-mount-helper-ec2-mac.md "mounting-fs-mount-helper-ec2-mac.md")
- [Mounting EFS file systems from a different AWS Region](mount-different-region.md "mount-different-region.md")
- [Mounting One Zone file systems](mounting-one-zone.md "mounting-one-zone.md")
- [Mounting with IAM authorization](mounting-IAM-option.md "mounting-IAM-option.md")
- [Mounting with EFS access points](mounting-access-points.md "mounting-access-points.md")
- [Mounting EFS to multiple
  EC2 instances](mount-multiple-ec2-instances.md "mount-multiple-ec2-instances.md")
- [Mounting EFS file systems from
  another AWS account or VPC](manage-fs-access-vpc-peering.md "manage-fs-access-vpc-peering.md")
