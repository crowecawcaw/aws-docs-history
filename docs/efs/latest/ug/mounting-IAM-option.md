# Mounting with IAM authorization

To mount your EFS file system on Linux instances using AWS Identity and Access Management (IAM)
authorization, use the EFS mount helper. For more information about IAM
authorization for NFS clients, see [Using IAM to control access to file
systems](iam-access-control-nfs-efs.md "iam-access-control-nfs-efs.md").

You need to create a directory to use as the file system mount point in the following sections. You can use the following command
to create a mount point directory `efs`:

```
sudo mkdir efs
```

You can then replace instances of `efs-mount-point` with `efs`.

## Mounting with IAM using an EC2 instance

profile

If you are mounting with IAM authorization to an Amazon EC2 instance with an instance profile,
use the `tls` and `iam` mount options, shown following.

```
`$` sudo mount -t efs -o tls,iam `file-system-id` `efs-mount-point`/
```

To automatically mount with IAM authorization to an EC2 instance that has an
instance profile, add the following line to the `/etc/fstab` file on
the EC2 instance.

```
`file-system-id`:/ `efs-mount-point` efs _netdev,tls,iam 0 0
```

## Mounting with IAM using a named profile

You can mount with IAM authorization using the IAM credentials located in the
AWS CLI credentials file `~/.aws/credentials`, or the AWS CLI config file
`~/.aws/config`. If `"awsprofile"` is not specified, the
"default" profile is used.

To mount with IAM authorization to a Linux instance using a credentials file,
use the `tls`, `awsprofile`, and `iam` mount options, shown following.

```
`$` sudo mount -t efs -o tls,iam,awsprofile=`namedprofile` `file-system-id` `efs-mount-point`/
```

To automatically mount with IAM authorization to a Linux instance using a
credentials file, add the following line to the `/etc/fstab` file on
the EC2 instance.

```
`file-system-id`:/ `efs-mount-point` efs _netdev,tls,iam,awsprofile=`namedprofile` 0 0
```
