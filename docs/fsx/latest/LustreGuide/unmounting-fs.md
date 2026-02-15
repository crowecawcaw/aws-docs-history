# Unmounting file systems

Before deleting an FSx for Lustre file system, ensure it is unmounted from all Amazon EC2 instances
that have mounted it, and before shutting down or terminating any Amazon EC2 instance, ensure any
mounted FSx for Lustre file systems are unmounted from that instance.

FSx for Lustre servers grant temporary file and directory locks to clients during I/O operations,
and clients must respond promptly when servers ask clients to release their locks to unblock I/O
operations from other clients. If clients become non-responsive, they may be forcefully evicted
after several minutes to allow other clients to proceed with their requested I/O operations.
To avoid these waiting periods, you should always unmount the file system from client instances
before shutting down or terminating them, and before deleting FSx for Lustre file systems.

You can unmount a file system on your Amazon EC2 instance by running the `umount`
command on the instance itself. You can't unmount an Amazon FSx file system through the AWS CLI, the
AWS Management Console, or through any of the AWS SDKs. To unmount an Amazon FSx file system connected to an
Amazon EC2 instance running Linux, use the `umount` command as follows:

```
umount `/mnt/fsx`
```

We recommend that you do not specify any other `umount` options. Avoid setting
any other `umount` options that are different from the defaults.

You can verify that your Amazon FSx file system has been unmounted by running the
`df` command. This command displays the disk usage statistics for the file
systems currently mounted on your Linux-based Amazon EC2 instance. If the Amazon FSx file system that
you want to unmount isn’t listed in the `df` command output, this means that the
file system is unmounted.

###### Example– Identify the mount status of an Amazon FSx file system and unmount it

```
$ df -T
Filesystem Type 1K-blocks Used Available Use% Mounted on
`file-system-id`.fsx.`aws-region`.amazonaws.com@tcp:/`mountname` /fsx 3547708416 61440 3547622400 1% /fsx
      /dev/sda1 ext4 8123812 1138920 6884644 15% /
```

```
$ umount /fsx
```

```
$ df -T
```

```
Filesystem Type 1K-blocks Used Available Use% Mounted on
/dev/sda1 ext4 8123812 1138920 6884644 15% /
```
