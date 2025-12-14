# Troubleshooting Amazon EFS performance

issues

In general, if you encounter issues with Amazon EFS that
you have trouble resolving, confirm that you're using a recent Linux kernel. If you are
using an enterprise Linux distribution, we recommend the following:

- Amazon Linux 2 with kernel 5.10.245-243 or newer
- Amazon Linux 2023 or newer
- RHEL 7.3 or newer
- All versions of Ubuntu 16.04
- Ubuntu 14.04 with kernel 3.13.0-83 or newer
- SLES 12 Sp2 or later
  If you are using another distribution or a custom kernel, we recommend kernel version
  5.10.245-243 or newer.

###### Note

You may experience slower than normal read performance after renaming files on your EFS file system when using NFSv4 due to [Slow reads after renaming files (NFSv4 attribute cache issue)](#nfsv4-rename-cache-issue "#nfsv4-rename-cache-issue").

###### Topics

- [Slow reads after renaming files (NFSv4 attribute cache issue)](#nfsv4-rename-cache-issue "#nfsv4-rename-cache-issue")
- [Unable to create an EFS file system](#cant-create-filesystem "#cant-create-filesystem")
- [Access denied to allowed files on NFS file system](#nfs-16-group-limit "#nfs-16-group-limit")
- [Errors when accessing the Amazon EFS console](#efs-console-access-errors "#efs-console-access-errors")
- [Amazon EC2 instance hangs](#ec2-instance-hangs "#ec2-instance-hangs")
- [Application writing large amounts of
  data hangs](#application-large-data-hangs "#application-large-data-hangs")
- [Poor performance when opening
  many files in parallel](#open-close-operations-serialized "#open-close-operations-serialized")
- [Custom NFS settings causing write
  delays](#custom-nfs-settings-write-delays "#custom-nfs-settings-write-delays")
- [Creating backups with Oracle Recovery Manager
  is slow](#oracle-backup-slow "#oracle-backup-slow")

## Slow reads after renaming files (NFSv4 attribute cache issue)

You may experience slower than normal read performance after renaming files on your EFS file system when using NFSv4. This is caused by improper attribute cache handling in the Linux kernel, which results in excessive GETATTR operations for renamed files.

**Kernel versions with this bug**

Amazon Linux 2:

- kernel-5.10.242-239.961.amzn2
- kernel-5.10.244-240.965.amzn2
- kernel-5.10.244-240.970.amzn2
- kernel-5.10.245-241.976.amzn2
- kernel-5.10.245-241.978.amzn2

**Action to take**

Update your kernel to the latest version. For Amazon Linux 2, kernel version kernel-5.10.245-243.979.amzn2 or later contains the fix.

For Amazon Linux 2, run the following commands:

```
sudo yum -y install `latest version`
sudo reboot
```

For other Linux distributions, check with your distribution vendor for kernel updates that address this NFSv4 attribute cache issue.

## Unable to create an EFS file system

A request to create an EFS file system fails with the following message:

```
`User: arn:aws:iam::111122223333:user/`username` is not authorized to
perform: elasticfilesystem:CreateFileSystem on the specified resource.`
```

###### Action to take

Check your AWS Identity and Access Management (IAM) policy to confirm that you are authorized to
create EFS file systems with the specified resource conditions. For more
information, see [Identity and access management for Amazon EFS](security-iam.md "security-iam.md").

## Access denied to allowed files on NFS file system

When a user who is assigned more than 16 access group IDs (GIDs) attempts to
perform an operation on an NFS file system, they could be denied access to allowed
files on the file system. This issue occurs because the NFS protocol supports a
maximum of 16 GIDs per user, and any additional GIDs are truncated from the NFS
client request, as defined in [RFC 5531](https://www.rfc-editor.org/rfc/rfc5531 "https://www.rfc-editor.org/rfc/rfc5531").

###### Action to take

Restructure your NFS user and group mappings so that each user is assigned no
more than 16 access groups (GIDs).

## Errors when accessing the Amazon EFS console

This section describes errors users might experience when accessing the Amazon EFS management console.

### Error authenticating credentials for `ec2:DescribeVPCs`

The following error message displays when accessing the Amazon EFS console:

```
`AuthFailure: An error occurred authenticating your credentials for ec2:DescribeVPCs.`
```

This error indicates that your login credentials did not successfully authenticate with the Amazon EC2 service.
The Amazon EFS console calls the Amazon EC2 service on your behalf when creating EFS file systems in the VPC that you choose.

###### Action to take

Ensure that the time on the client accessing the Amazon EFS console is set correctly.

## Amazon EC2 instance hangs

An Amazon EC2 instance can hang because you deleted a file system mount target without
first unmounting the file system.

###### Action to take

Before you delete a file system mount target, unmount the file system. For
more information about unmounting your Amazon EFS file system, see [Unmounting file systems](unmounting-fs.md "unmounting-fs.md").

## Application writing large amounts of

data hangs

An application that writes a large amount of data to Amazon EFS hangs and causes the
instance to reboot.

**Action to take**

If an application takes too long to write all of its data to Amazon EFS, Linux might
reboot because it appears that the process has become unresponsive. Two kernel
configuration parameters define this behavior, `kernel.hung_task_panic`
and `kernel.hung_task_timeout_secs`.

In the example following, the state of the hung process is reported by the
`ps` command with `D` before the instance reboot,
indicating that the process is waiting on I/O.

```
$ ps aux | grep large_io.py
root 33253 0.5 0.0 126652 5020 pts/3 D+ 18:22 0:00 python large_io.py
/efs/large_file
```

To prevent a reboot, increase the timeout period or disable kernel panics when a
hung task is detected. The following command disables hung task kernel panics on
most Linux systems.

```
$ sudo sysctl -w kernel.hung_task_panic=0
```

## Poor performance when opening

many files in parallel

Applications that open multiple files in parallel do not experience the expected
increase in performance of I/O parallelization.

**Action to take**

This issue occurs on Network File System version 4 (NFSv4) clients and on RHEL 6
clients using NFSv4.1 because these NFS clients serialize NFS OPEN and CLOSE
operations. Use NFS protocol version 4.1 and one of the suggested [Linux distributions](#recommend.linux.dist "#recommend.linux.dist") that does not have
this issue.

If you can't use NFSv4.1, be aware that the Linux NFSv4.0 client serializes open
and close requests by user ID and group IDs. This serialization happens even if
multiple processes or multiple threads issue requests at the same time. The client
only sends one open or close operation to an NFS server at a time, when all of the
IDs match. To work around these issues, you can perform any of the following
actions:

- You can run each process from a different user ID on the same Amazon EC2
  instance.
- You can leave the user IDs the same across all open requests, and modify
  the set of group IDs instead.
- You can run each process from a separate Amazon EC2 instance.

## Custom NFS settings causing write

delays

You have custom NFS client settings, and it takes up to three seconds for an Amazon EC2
instance to see a write operation performed on a file system from another Amazon EC2
instance.

**Action to take**

If you encounter this issue, you can resolve it in one of the following
ways:

- If the NFS client on the Amazon EC2 instance that's reading data has attribute
  caching activated, unmount your file system. Then remount it with the
  `noac` option to disable attribute caching. Attribute caching
  in NFSv4.1 is enabled by default.

###### Note

Disabling client-side caching can potentially reduce your
application's performance.

- You can also clear your attribute cache on demand by using a programming
  language compatible with the NFS procedures. To do this, you can send an
  `ACCESS` procedure request immediately before a read
  request.

For example, using the Python programming language, you can construct the
following call.

```
# Does an NFS ACCESS procedure request to clear the attribute cache, given a path to the file
import os
os.access(path, os.W_OK)
```

## Creating backups with Oracle Recovery Manager

is slow

Creating backups with Oracle Recovery Manager can be slow if Oracle Recovery
Manager pauses for 120 seconds before starting a backup job.

**Action to take**

If you encounter this issue, disable Oracle Direct NFS, as described in [Enabling and Disabling Direct NFS Client Control of NFS](https://docs.oracle.com/database/122/HPDBI/enabling-and-disabling-direct-nfs-client-control-of-nfs.htm "https://docs.oracle.com/database/122/HPDBI/enabling-and-disabling-direct-nfs-client-control-of-nfs.htm") in the Oracle
Help Center.

###### Note

Amazon EFS doesn't support Oracle Direct NFS.
