# Unmounting file systems

Before you delete a file system, we recommend that you unmount it from every Amazon EC2
instance that it's connected to. You can unmount a file system on your Amazon EC2 instance by
running the `umount` command on the instance itself. You can't unmount an
EFS file system through the AWS CLI, the AWS Management Console, or through any of the AWS SDKs.
To unmount an EFS file system connected to an EC2 instance running Linux,
use the `umount` command as follows:

```
umount `/mnt/efs`
```

We recommend that you do not specify any other `umount` options. Avoid
setting any other `umount` options that are different from the defaults.

You can verify that your EFS file system has been unmounted by running the
`df` command. This command displays the disk usage statistics for the file
systems currently mounted on your Linux-based Amazon EC2 instance. If the EFS file
system that you want to unmount isn’t listed in the `df` command output, this means
that the file system is unmounted.

###### Example – Identify the mount status of an EFS file system and unmount

it

```
$ df -T
Filesystem Type 1K-blocks Used Available Use% Mounted on
/dev/sda1 ext4 8123812 1138920 6884644 15% /
`availability-zone`.`file-system-id`.efs.`aws-region`.amazonaws.com :/ nfs4 9007199254740992 0 9007199254740992 0% /mnt/efs

```

```
$ umount /mnt/efs
```

```
$ df -T
```

```
Filesystem Type 1K-blocks Used Available Use% Mounted on
/dev/sda1 ext4 8123812 1138920 6884644 15% /
```
