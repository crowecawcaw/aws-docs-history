# Configuring and using Mountpoint

To use Mountpoint for Amazon S3, your host needs valid AWS credentials with access to the Amazon S3 bucket or
buckets that you would like to mount. For different ways to authenticate, see
Mountpoint [AWS Credentials](https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#aws-credentials "https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#aws-credentials") on GitHub.

For example, you can create a new AWS Identity and Access Management (IAM) user and role for this purpose. Make
sure that this role has access to the bucket or buckets that you would like to mount. You can
[pass the
IAM role](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md") to your Amazon EC2 instance with an instance profile.

###### Topics

- [Using Mountpoint for Amazon S3](#using-mountpoint "#using-mountpoint")
- [Configuring caching in Mountpoint](#mountpoint-caching "#mountpoint-caching")

## Using Mountpoint for Amazon S3

Use Mountpoint for Amazon S3 to do the following:

1. Mount your Amazon S3 buckets.
   1. You can mount Amazon S3 buckets manually by using the `mount-s3` command.

   In the following example, replace
   `amzn-s3-demo-bucket` with the name of your S3
   bucket, and replace `~/mnt` with the directory on
   your host where you want your S3 bucket to be mounted.

   ```
   mkdir `~/mnt`
   mount-s3 ``amzn-s3-demo-bucket`` `~/mnt`
   ```

   Because the Mountpoint client runs in the background by default, the
   `~/mnt` directory now gives you access to the
   objects in your Amazon S3 bucket. 2. Alternatively, you can configure automatic mounting of Amazon S3 buckets when an instance starts up or reboots.

   For existing or running Amazon EC2 instances, find the `fstab` file in the `/etc/fstab` directory of your Linux system. Then, add a line to your `fstab` file. For example, to mount `amzn-s3-demo-bucket` using the prefix `example-prefix/` to your sytem path `/mnt/mountpoint`, see the following. To use the following example, replace the `user input
 placeholders` with your own information.

   ```
   s3://``amzn-s3-demo-bucket``/`example-prefix`/ `/mnt/mountpoint` mount-s3 _netdev,nosuid,nodev,nofail,rw 0 0
   ```

   See the following table for an explanation of the options used in the example.

   | Option    | Description                                                                                                       |
   | --------- | ----------------------------------------------------------------------------------------------------------------- |
   | `_netdev` | Specifies that the filesystem requires networking to mount.                                                       |
   | `nosuid`  | Specifies that the filesystem cannot contain set user ID files.                                                   |
   | `nodev`   | Specifies that the filesystem cannot contain special devices.                                                     |
   | `nofail`  | Specifies that failure to mount the filesystem should still allow the system to boot.                             |
   | `rw`      | Specifies that the mount point is created with read and write permissions. Alternatively, use `ro` for read only. |

   For new Amazon EC2 instances, you can modify user data on an Amazon EC2 template and set up the `fstab` file as follows. To use the following example, replace the `user input
 placeholders` with your own information.

   ```
   #!/bin/bash -e
   MP_RPM=$(mktemp --suffix=.rpm)
   curl https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.rpm > $MP_RPM
   yum install -y $MP_RPM
   rm $MP_RPM

   MNT_PATH=/mnt/mountpoint
   echo "s3://``amzn-s3-demo-bucket``/ ${MNT_PATH} mount-s3 _netdev,nosuid,nodev,rw,allow-other,nofail" >> /etc/fstab
   mkdir $MNT_PATH

   systemctl daemon-reload
   mount -a

   ```

2. Access the objects in your Amazon S3 bucket through Mountpoint.

After you mount your bucket locally, you can use common Linux
commands, such as `cat` or `ls`, to work with your S3 objects.
Mountpoint for Amazon S3 interprets keys in your Amazon S3 bucket as file system paths by splitting them on
the forward slash (`/`) character. For example, if you have the object key
`Data/2023-01-01.csv` in your bucket, you will have a directory named
`Data` in your Mountpoint file system, with a file named
`2023-01-01.csv` inside it.

Mountpoint for Amazon S3 intentionally does not implement the full [POSIX](https://en.wikipedia.org/wiki/POSIX "https://en.wikipedia.org/wiki/POSIX") standard specification for
file systems. Mountpoint is optimized for workloads that need high-throughput
read and write access to data stored in Amazon S3 through a file system interface, but that
otherwise do not rely on file system features. For more information, see Mountpoint for Amazon S3
[file
system behavior](https://github.com/awslabs/mountpoint-s3/blob/main/doc/SEMANTICS.md "https://github.com/awslabs/mountpoint-s3/blob/main/doc/SEMANTICS.md") on GitHub. Customers that need richer file
system semantics should consider other AWS file services, such as [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") or [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/"). 3. Unmount your Amazon S3 bucket by using the `umount` command. This command unmounts
your S3 bucket and exits Mountpoint.

To use the following example command, replace
`~/mnt` with the directory on your host where
your S3 bucket is mounted.

```
umount `~/mnt`
```

###### Note

To get a list of options for this command, run `umount --help`.

For additional Mountpoint configuration details, see [Amazon S3 bucket configuration](https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#s3-bucket-configuration "https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#s3-bucket-configuration"), and [file system configuration](https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#file-system-configuration "https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#file-system-configuration") on GitHub.

## Configuring caching in Mountpoint

Mountpoint for Amazon S3 supports different types of data caching. To accelerate repeated read
requests, you can opt in to the following:

- **Local cache** – You can use a local cache in
  your Amazon EC2 instance storage or an Amazon Elastic Block Store volume. If you repeatedly read the same data
  from the same compute instance and if you have unused space in your local instance
  storage for the repeatedly read dataset, you should opt in to a local cache.
- **Shared cache** – You can use a shared cache on
  S3 Express One Zone. If you repeatedly read small objects from multiple compute instances or if
  you do not know the size of your repeatedly read dataset and want to benefit from
  elasticity of cache size, you should opt in to the shared cache. Once you opt in,
  Mountpoint retains objects with sizes up to one megabyte in a directory bucket
  that uses S3 Express One Zone.
- **Combined local and shared cache** – If you
  have unused space in your local cache but also want a shared cache across multiple
  instances, you can opt in to both a local cache and shared cache.

Caching in Mountpoint is ideal for use cases where you repeatedly read the same
data that doesn’t change during the multiple reads. For example, you can use caching with
machine learning training jobs that need to read a training dataset multiple times to
improve model accuracy.

For more information about how to configure caching in Mountpoint, see the
following examples.

###### Topics

- [Local cache](#local-cache-example "#local-cache-example")
- [Shared cache](#shared-cache-example "#shared-cache-example")
- [Combined local and shared cache](#shared-local-cache-example "#shared-local-cache-example")

### Local cache

You can opt in to a local cache with the `--cache
 `CACHE_PATH`flag. In the following example, replace
`CACHE_PATH`with the filepath to the directory
 that you want to cache your data in. Replace
 ```amzn-s3-demo-bucket``` with the name of your Amazon S3
 bucket, and replace`~/mnt`` with the directory on
your host where you want your S3 bucket to be mounted.

```
mkdir `~/mnt`
mount-s3 --cache `CACHE_PATH` ``amzn-s3-demo-bucket`` `~/mnt`
```

When you opt in to local caching while mounting an Amazon S3 bucket, Mountpoint creates an
empty sub-directory at the configured cache location, if that sub-directory doesn’t
already exist. When you first mount a bucket and when you unmount, Mountpoint deletes the
contents of the local cache.

###### Important

If you enable local caching, Mountpoint will persist unencrypted object
content from your mounted Amazon S3 bucket at the local cache location provided at mount. In
order to protect your data, you should restrict access to the data cache location by
using file system access control mechanisms.

### Shared cache

If you repeatedly read small objects (up to 1 MB) from multiple compute instances or
the size of the dataset that you repeatedly read often exceeds the size of your local
cache, you should use a shared cache in [S3 Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/ "https://aws.amazon.com/s3/storage-classes/express-one-zone/"). When you read the same
data repeatedly from multiple instances, this improves latency by avoiding redundant
requests to your mounted Amazon S3 bucket.

Once you opt in to the shared cache, you pay for the data cached in your
directory bucket in S3 Express One Zone. You also pay for requests made against your data in the
directory bucket in S3 Express One Zone. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). Mountpoint never deletes cached objects
from directory buckets. To manage your storage costs, you should set up a [Lifecycle
policy on your directory bucket](directory-buckets-objects-lifecycle.md "directory-buckets-objects-lifecycle.md") so that Amazon S3 expires the cached data in
S3 Express One Zone after a period of time that you specify. For more information, see [Mountpoint for Amazon S3 caching configuration](https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#caching-configuration "https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#caching-configuration") on GitHub.

To opt in to caching in S3 Express One Zone when you mount an Amazon S3 bucket to your compute
instance, use the `--cache-xz` flag and specify a directory bucket as your
cache location. In the following example, replace the `user input
 placeholders`.

```
mount-s3 `amzn-s3-demo-bucket` `~/mnt` --cache-xz ``amzn-s3-demo-bucket--usw2-az1--x-s3``
```

### Combined local and shared cache

If you have unused space on your instance but you also want to use a shared cache
across multiple instances, you can opt in to both a local cache and shared cache. With
this caching configuration, you can avoid redundant read requests from the same instance
to the shared cache in directory bucket when the required data is cached in local
storage. This can reduce request costs and improve performance.

To opt in to both a local cache and shared cache when you mount an Amazon S3 bucket, you
specify both cache locations by using the `--cache` and `--cache-xz`
flags. To use the following example to opt into both a local and shared cache, replace the
`user input placeholders`.

```
mount -s3 `amzn-s3-demo-bucket` `~/mnt` --cache `/path/to/mountpoint/cache` --cache -xz ``amzn-s3-demo-bucket--usw2-az1--x-s3``
```

For more information, [Mountpoint for Amazon S3 caching configuration](https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#caching-configuration "https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#caching-configuration") on GitHub.

###### Important

If you enable shared caching, Mountpoint will copy object content from your
mounted Amazon S3 bucket into the S3 directory bucket that you provide as your shared cache
location, making it accessible to any caller with access to the S3 directory bucket. To
protect your cached data, you should follow the [Security best practices for Amazon S3](security-best-practices.md "security-best-practices.md") to ensure that your buckets use the correct
policies and are not publicly accessible. You should use a directory bucket dedicated
to Mountpoint shared caching and grant access only to Mountpoint
clients.
