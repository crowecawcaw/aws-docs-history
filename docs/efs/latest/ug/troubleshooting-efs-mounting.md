# Troubleshooting mount issues

Following, you can find information about troubleshooting EFS file
system mounting issues.

## File system mount on Windows instance

fails

A file system mount on an Amazon EC2 instance on Microsoft Windows fails.

###### Action to take

Don't use Amazon EFS with Windows EC2 instances, which isn't supported.

## Access denied by server

A file system mount fails with the following message:

```
/efs mount.nfs4: access denied by server while mounting 127.0.0.1:/
```

This issue can occur if your NFS client does not have permission to mount the file system.

###### Action to take

If you are attempting to mount the file system using IAM, make sure you are
using the `-o iam` or -o tls option in your mount command. This tells the EFS
mount helper to pass your credentials to the EFS mount target. If you still
don't have access, check your file system policy and your identity policy
to ensure there are no DENY clauses that apply to your connection, and that
there is at least one ALLOW clause that applies to the connection. For more
information, see [Using IAM to control access to file
systems](iam-access-control-nfs-efs.md "iam-access-control-nfs-efs.md") and [Creating file system policies](create-file-system-policy.md "create-file-system-policy.md").

## Automatic mounting fails and the instance is

unresponsive

This issue can occur if the file system was mounted automatically on an instance
and the `_netdev` option wasn't declared. If `_netdev` is
missing, your EC2 instance might stop responding. This result is because network
file systems need to be initialized after the compute instance starts its
networking.

###### Action to take

If this issue occurs, contact AWS Support.

## Mounting multiple Amazon EFS file systems in

/etc/fstab fails

For instances that use the systemd init system with two or more Amazon EFS entries at
`/etc/fstab`, there might be times where some or all of these
entries are not mounted. In this case, the `dmesg` output shows one or
more lines similar to the following.

```
`NFS: nfs4_discover_server_trunking unhandled error -512. Exiting with error EIO`
```

###### Action to take

In this case, we recommend that you create a new systemd service file in
`/etc/systemd/system/mount-nfs-sequentially.service`. The
code to include in the file depends on whether you are manually mounting the
file systems or using the Amazon EFS mount helper.

- If you are manually mounting the file systems, then the `ExecStart` command must
  point to Network File System (NFS4). Include the following code in the
  file:

```
[Unit]
Description=Workaround for mounting NFS file systems sequentially at boot time
After=remote-fs.target

[Service]
Type=oneshot
ExecStart=/bin/mount -avt nfs4
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

- If you are using the Amazon EFS mount helper, then the `ExecStart` command must point to
  EFS instead of NFS4 to use Transport Layer Security (TLS). Include the
  following code in the file:

```
[Unit]
Description=Workaround for mounting NFS file systems sequentially at boot time
After=remote-fs.target

[Service]
Type=oneshot
ExecStart=/bin/mount -avt efs
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

After you create the file, run the following two commands:

1. `sudo systemctl daemon-reload`
2. `sudo systemctl enable mount-nfs-sequentially.service`

Then restart your Amazon EC2 instance. The file systems are mounted on demand,
generally within a second.

## Mount command fails with "wrong fs type"

error message

The mount command fails with the following error message.

```
mount: wrong fs type, bad option, bad superblock on 10.1.25.30:/,
missing codepage or helper program, or other error (for several filesystems
(e.g. nfs, cifs) you might need a /sbin/mount.<type> helper program)
In some cases useful info is found in syslog - try dmesg | tail or so.

```

###### Action to take

If you receive this message, install the `nfs-utils` (or
`nfs-common` on Ubuntu) package. For more information, see [Installing the NFS client](mounting-fs-install-nfsclient.md "mounting-fs-install-nfsclient.md").

## Mount command fails with "incorrect

mount option" error message

The mount command fails with the following error message.

```
mount.nfs: an incorrect mount option was specified
```

###### Action to take

This error message most likely means that your Linux distribution doesn't
support Network File System versions 4.0 and 4.1 (NFSv4). To confirm this is the
case, you can run the following command.

```
`$` grep CONFIG_NFS_V4_1 /boot/config*
```

If the preceding command returns `# CONFIG_NFS_V4_1 is not set`,
NFSv4.1 is not supported on your Linux distribution. For a list of the Amazon
Machine Images (AMIs) for Amazon Elastic Compute Cloud (Amazon EC2) that support NFSv4.1, see [NFS support](mounting-fs-old.md#mounting-fs-nfs-info "mounting-fs-old.md#mounting-fs-nfs-info").

## Mounting with access point fails

The mount command fails when mounting with an access point, with the following error message:

```
mount.nfs4: mounting `access_point` failed, reason given by server: No such file or directory
```

###### Action to take

This error message indicates that the specified EFS path does not exist. Make sure that you provide the ownership and permissions for the
access point root directory. EFS will not create the root directory without this information. For more information, see
[Working with access points](efs-access-points.md "efs-access-points.md").

If you don't specify any root directory ownership and permissions, and the root
directory does not already exist, EFS will not create the root directory. When this happens,
any attempts to mount the file system using the access point will fail.

## File system mount fails immediately after

file system creation

It can take up to 90 seconds after creating a mount target for the Domain Name
Service (DNS) records to propagate fully in an AWS Region.

###### Action to take

If you're programmatically creating and mounting file systems, for example
with an CloudFormation template, we recommend that you implement a wait condition.

## File system mount hangs and then fails

with timeout error

The file system mount command hangs for a minute or two, and then fails with a
timeout error. The following code shows an example.

```
$ sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport `mount-target-ip`:/ mnt

*[2+ minute wait here]*
mount.nfs: Connection timed out
$Â 
```

**Action to take**

This error can occur because either the Amazon EC2 instance or the mount target
security groups are not configured properly. Make sure that the mount target
security group has an inbound rule
that allows NFS access on port 2049 from the EC2 security group. For more information, see [Using VPC security groups](network-access.md "network-access.md").

Verify that the mount target IP address that you specified is valid. If you
specify the wrong IP address and there is nothing else at that IP address to reject
the mount, you might experience this issue.

## File system mount with NFS using DNS name fails

Attempts to mount a file system using an NFS client (not using the `amazon-efs-utils` client) using the file system's DNS name fails,
as shown in the following example:

```
$ sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport `file-system-id`.efs.`aws-region`.amazonaws.com:/ mnt
mount.nfs: Failed to resolve server `file-system-id`.efs.`aws-region`.amazonaws.com:
  Name or service not known.

$ 
```

**Action to take**

Check your VPC configuration. If you are using a custom VPC, make sure that DNS
settings are enabled. For more information, see [DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the
_Amazon VPC User Guide_. Also, file system and mount target DNS
names are not resolvable from outside the VPC where they exist.

Before you can mount a file system using its DNS name in the `mount` command, you must do the
following:

- Ensure that there's an Amazon EFS mount target in the same Availability Zone as
  the Amazon EC2 instance.
- Ensure that there's a mount target in the same VPC as the Amazon EC2 instance.
  Otherwise, you can't use DNS name resolution for EFS mount targets that are in another VPC. For more information, see
  [Mounting EFS file systems from
  another AWS account or VPC](manage-fs-access-vpc-peering.md "manage-fs-access-vpc-peering.md").
- Connect your Amazon EC2 instance inside an Amazon VPC configured to use the DNS
  server provided by Amazon. For more information, see
  [DHCP option sets in Amazon VPC](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in
  the _Amazon VPC User Guide_.
- Ensure that the Amazon VPC of the connecting Amazon EC2 instance has DNS hostnames
  enabled. For more information, see
  [DNS attributes in your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support") in the
  _Amazon VPC User Guide_.

## File system mount fails with "nfs

not responding"

An Amazon EFS file system mount fails on a Transmission Control Protocol (TCP)
reconnection event with `"nfs: server_name still not responding"`.

**Action to take**

Use the `noresvport` mount option to make sure that the NFS client uses
a new TCP source port when a network connection is reestablished. Doing this helps
ensure uninterrupted availability after a network recovery event.

## Mount target lifecycle state is

stuck

The mount target lifecycle state is stuck in the **creating** or
**deleting** state.

###### Action to take

Retry the `CreateMountTarget` or `DeleteMountTarget`
call.

## Mount target lifecycle state shows

error

The mount target lifecycle state shows as **error**.

**Action to take**

Amazon EFS cannot create the necessary Domain Name System (DNS)  records for new file
system mount targets if the virtual private cloud (VPC) has conflicting hosted
zones. Amazon EFS cannot create new records within a customer-owned hosted zone. If you
need to maintain a hosted zone with a conflicting
`efs.`<region>`.amazonaws.com` DNS
range, create the hosted zone in a separate VPC. For more information about DNS
considerations for VPC, see
[DNS
attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md").

To resolve this issue, delete the conflicting
`efs.`<region>`.amazonaws.com` host
from the VPC and create the mount target again. For more information about deleting
the mount target, see [Managing mount targets](accessing-fs.md "accessing-fs.md").

## Mount does not respond

An Amazon EFS mount appears unresponsive. For example, commands like `ls`
hang.

**Action to take**

This error can occur if another application is writing large amounts of data to
the file system. Access to the files that are being written might be blocked until
the operation is complete. In general, any commands or applications that attempt to
access files that are being written to might appear to hang. For example, the
`ls` command might hang when it gets to the file that is being
written. This result is because some Linux distributions alias the `ls`
command so that it retrieves file attributes in addition to listing the directory
contents.

To resolve this issue, verify that another application is writing files to the
Amazon EFS mount, and that it is in the `Uninterruptible sleep`
(`D`) state, as in the following example:

```
$ ps aux | grep large_io.py
root 33253 0.5 0.0 126652 5020 pts/3 D+ 18:22 0:00 python large_io.py /efs/large_file
```

After you've verified that this is the case, you can address the issue by waiting
for the other write operation to complete, or by implementing a workaround. In the
example of `ls`, you can use the `/bin/ls` command directly,
instead of an alias. Doing this allows the command to proceed without hanging on the
file being written. In general, if the application writing the data can force a data
flush periodically, perhaps by using `fsync(2)`, doing so can help
improve the responsiveness of your file system for other applications. However, this
improvement might be at the expense of performance when the application writes
data.

## Mounted client gets disconnected

A client mounted to an Amazon EFS file system can occasionally become disconnected due to any number of causes.
NFS clients are designed to automatically reconnect in case of interruption to minimize the impact of routine
disconnections on application performance and availability. In most cases, clients transparently reconnect within seconds.

However, the NFS client software included in older versions of the Linux kernel (versions v5.4 and below) include a
behavior that causes NFS clients to, upon disconnection, attempt reconnecting on the same TCP source port. This behavior
does not comply with the TCP RFC, and can prevent these clients from quickly re-establishing connections to their NFS
server (in this case, an EFS file system).

To resolve this issue, we strongly recommend that you use the Amazon EFS mount helper to mount your EFS file systems.
The EFS mount helper uses mount settings that are optimized for Amazon EFS file systems. For more information about the EFS client
and mount helper, see [Installing the Amazon EFS client](using-amazon-efs-utils.md "using-amazon-efs-utils.md").

If you can't use the EFS mount helper, we strongly recommend using the `noresvport` NFS mount option,
which instructs NFS clients to re-establish connections using new TCP source ports to avoid this issue.
For more information, see [Recommended NFS mount settings](mounting-fs-nfs-mount-settings.md "mounting-fs-nfs-mount-settings.md").

## Operations on newly mounted file

system return "bad file handle" Error

Operations performed on a newly mounted file system return a `bad file
 handle` error.

This error can happen if an Amazon EC2 instance was connected to one file system and
one mount target with a specified IP address, and then that file system and mount
target were deleted. If you create a new file system and mount target to connect to
that Amazon EC2 instance with the same mount target IP address, this issue can occur.

###### Action to take

You can resolve this error by unmounting the file system, and then remounting
the file system on the Amazon EC2 instance. For more information about unmounting
your Amazon EFS file system, see [Unmounting file systems](unmounting-fs.md "unmounting-fs.md").

## Unmounting a file system fails

If your file system is busy, you can't unmount it.

###### Action to take

You can resolve this issue in the following ways:

- Use lazy unmount, **umount -l** which detaches the file system from the file
  system hierarchy when run, then cleans up all references to the file system
  as soon as it is not busy anymore.
- Wait for all read and write operations to finish, and then attempt the
  **umount** command again.
- Force an unmount using the **umount -f** command.

###### Warning

Forcing an unmount interrupts any data read or write operations that
are currently in process for the file system. See the
[umount man page](https://man7.org/linux/man-pages/man8/umount.8.html "https://man7.org/linux/man-pages/man8/umount.8.html")
for more information and guidance when using this option.
